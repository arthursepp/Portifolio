const express = require('express');
const router = express.Router()
const Proprietario = require('../models/Proprietario')

// Listando todos os proprietários:
router.get('/', async (req, res) => {
    try {
        // Busca todos os proprietários:
        const proprietarios = await Proprietario.find()
        // Retorna a lista de proprietários em formato JSON:
        res.json(proprietarios)
    } catch (err) {
        // Se houver erro, retorna o erro:
        res.status(500).send(err)
    }
})

// Buscando um proprietario por seu ID:
router.get('/:id', async (req, res) => {
    try {
        // Busca um proprietário pelo ID:
        const proprietario = await Proprietario.findById(req.params.id)
        // Se o proprietário for encontrado, retorna o código 200 (sucesso):
        res.status(200).json(proprietario)

    } catch(error) {
        // Se houver erro na busca, retorna o erro:
        res.status(500).json({ message: error.message })
    }
})

// Rota para o cadastro de um novo proprietario:
router.post('/', async (req, res) => {
    try {
        // Recebe os seguintes dados do corpo da requisição:
        const { nome, cpf, veiculos } = req.body
        // Cria um novo proprietário com os dados recebidos:
        const newProprietario = new Proprietario({
            nome,
            cpf,
            veiculos
        })

        // Salva o novo proprietário no banco de dados:
        await newProprietario.save()
        // Retorna uma mensagem de sucesso:
        res.status(201).json({ message: 'Proprietario cadastrado com sucesso!' })
    } catch (error) {
        res.status(500).json({ message: error.message })
    }
})

// Deletando um proprietário específico:
router.delete('/:id', async (req, res) => {
    try {
        // Busca um proprietário pelo ID e o deleta:
        await Proprietario.findByIdAndDelete(req.params.id)
        res.status(200).json({ message: 'Proprietario deletado com sucesso!' })
    } catch (error) {
        res.status(500).json({ message: error.message})
    }
})

// Atualizando um proprietário específico por seu ID:
router.put('/:id', async (req, res) => {
    try {
        // Pegando os dados do corpo da requisição:
        const { nome, cpf, veiculos } = req.body
        
        // Atualizando o proprietário pelo ID:
        await Proprietario.findByIdAndUpdate(req.params.id, { nome, cpf, veiculos })

        // Retornando uma mensagem de sucesso:
        res.status(200).json({ message: 'Proprietario atualizado com sucesso!' })
    } catch (error) {
        // Se houver erro, retorna o erro:
        res.status(500).json({ message: error.message })
    }
})

module.exports = router
