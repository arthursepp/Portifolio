const express = require("express")
const cors = require("cors")
const axios = require("axios")
const multer = require("multer")
const FormData = require("form-data")
const fs = require("fs")

const app = express()
app.use(cors())
app.use(express.json())

const PORT = 3000

const upload = multer({ dest: '../API/static' }) // Salvando temporariamente o arquivo

app.post('/carregar-documento', upload.single('file'), async (req, res) => {
    try {
        // Abrindo o arquivo que foi enviado por multer para leitura binária
        const fileStream = fs.createReadStream(req.file.path)

        // Criando o FormData para enviar para a API Python
        const formData = new FormData()
        formData.append('file', fileStream, req.file.originalname)

        // Enviando o arquivo para a API Python
        const response = await axios.post('http://127.0.0.1:5000/carregar-documento', formData, {
            headers: formData.getHeaders()
        })

        res.json(response.data)
    } catch (error) {
        res.status(500).json({ erro: `Erro ao enviar dados para a API: ${error.message}` })
    }
})

app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`)
})
