const express = require('express')
const fs = require('fs-extra')
const jwt = require('jsonwebtoken')
const bcrypt = require('bcryptjs')
const cors = require('cors')

const app = express()
const PORT = 8000
const SECRET_ = 'super-secret-key'

app.use(express.json())
app.use(cors())

const DB_FILE = './data/db.json'

const readDB = async () => await fs.readJSON(DB_FILE)
const writeDB = async (data) => await fs.writeJSON(DB_FILE, data)

const authMiddleware = (roles) => (req, res, next) => {
    const token = req.headers.authorization?.split('')[1]
    if (!token)return res.status(401).json({ message: 'Acesso negado!' })

    try {
        const decoded = jwt.verify(token, SECRET_)
        if (!roles.includes(decoded.tipo)) return res.status(403).json({ error: 'Acesso negado!' })
        req.user = decoded
        next()
    } catch {
        res.status(401).json({ error: 'Token inválido' })
    }
}

// * Rota de cadastro
app.post('/cadastro', async (req, res) => {
    const { 
        nome,
        cpf,
        cnpj,
        cep,
        rua,
        numRes,
        tel,
        senha,
        tipo 
    } = req.body

    if (!['Cliente', 'Farmacia', 'Master'].includes(tipo)) {
        return res.status(400).json({ error: 'Tipo de usuário inválido!' })
    }

    const db = await readDB()
    const usuarios = db.usuarios

    if (cpf && usuarios.some((u) => u.cpf === cpf)) {
        return res.status(400).json({ error: 'Já existe alguém cadastrado com esse CPF!' })
    }
    else if ( telefone && usuarios.some((u) => u.telefone === telefone) ) {
        return res.status(400).json({ error: 'Este telefone já foi cadastrado por outra empresa!' })
    }

    if (cnpj && usuarios.some((u) => u.cnpj=== cnpj )) {
        return res.status(400).json({ error: 'Já existe uma empresa cadastrada com esse CNPJ!' })
    }
    else if ( telefone && usuarios.some((u) => u.telefone === telefone) ) {
        return res.status(400).json({ error: 'Este telefone já foi cadastrado por outra empresa!' })
    }

    const senhaEncriptada = await bcrypt.hash(senha, 10)
    const novoUsuario = {
        id: Date.now(),
        nome,
        cpf,
        cnpj,
        cep,
        rua,
        numRes,
        tel,
        senha: senhaEncriptada,
        tipo 
    }
    usuarios.push(novoUsuario)

    await writeDB({ ...db, usuarios })

    res.json({ message: 'Cadastro realizado com sucesso!' })
})

// * Rota de login:
app.post('/login', async(req, res) => {
    const { identificador, senha } = req.body
    const db = await readDB()
    const usuario = db.usuarios.find((u) => u.cpf === identificador || u.cnpj === identificador)

    const senhaValida = await bcrypt.compare(senha, usuario.senha)
    if (!senhaValida || !usuario) return res.status(400).json({ error: 'Usuário ou senha inválidos.' })

    const token = jwt.sign({ id: usuario.id, tipo: usuario.tipo }, SECRET_, { expiresIn: '1h' })

    res.json({ token, tipo: usuario.tipo })
})

// * Listando os produtos de uma farmácia:
app.get('/farmacias/:id/produtos', async (req, res) => {
    const db = await readDB()
    const produtos = db.produtos.filter((p) => farmaciaId == req.params.id)
    res.json(produtos)
})

// * Registrando um novo produto (Restrito para farmácia):
app.post('/produtos', authMiddleware(['Farmacia']), async (req, res) => {
    const { nome, preco, farmaciaId } = req.body
    const db = await readDB()

    if (db.usuarios.every((u) => u.id != farmaciaId || u.tipo !== 'Farmacia')) {
            return res.status(400).json({ error: 'Farmácia não encontrada!' })
    }

    const novoProduto = { id: Date.now(), nome, preco, farmaciaId }
    db.produtos.push(novoProduto)
    await writeDB(db)

    res.json({ message: 'Produto adicionado!' })
})

// * Adicionando um pedido (Restrito para cliente):
app.post('/pedidos', authMiddleware(['Cliente']), async (req, res) => {
    const { clienteId, produtos } = req.body
    const db = await readDB()

    if (db.usuarios.every((u) => u.id != clienteId || u.tipo !== 'Cliente')) {
        return res.status(400).json({ error: 'Cliente não encontrado.' })
    }

    const novoPedido = { id: Date.now(), clienteId, produtos, status: 'Pendente' }
    db.pedidos.push(novoPedido)
    await writeDB(db)

    res.json({ message: 'Pedido realizado!' })
})

// * Gerenciar pedidos (Restrito para farmácia):
app.get('/farmacia/:id/pedidos', authMiddleware(['Farmacia']), async(req, res) => {
    const db = await readDB()
    const pedidos = db.pedidos.filter((p) => p.clienteId === req.user.id)
    res.json(pedidos)
})

app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`))
