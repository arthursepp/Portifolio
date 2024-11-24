const express = require('express')
const app = express()
const handlebars = require('express-handlebars')
const userController = require('./controller/userController.js')

app.engine('handlebars', handlebars.engine({defaultLayout: 'main'}))
app.set('view engine', 'handlebars')

app.get('/', userController.renderUsers)

const port = 3000
app.listen(port, () => {
    console.log(`Servidor rodando na port ${port}!`)
})
