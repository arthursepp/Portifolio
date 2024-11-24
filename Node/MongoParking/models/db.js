const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/Estacionamento', {})

const db = mongoose.connection

db.on('error', console.error.bind(console, 'Erro de conexão com o banco de dados:'))

db.once('open', function() {
    console.log('Conexão com o banco de dados estabelecida com sucesso!')
})

module.exports = db