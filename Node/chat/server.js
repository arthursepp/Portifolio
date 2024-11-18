const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

app.use(express.static(path.join(__dirname, 'public')));

// Configuração do Socket.IO
io.on('connection', (socket) => {
    console.log('Usuário conectado');

    // Ouve o evento de mensagem do cliente
    socket.on('chat message', (msg) => {
        console.log('Mensagem recebida:', msg);
        // Envia a mensagem para todos os clientes conectados
        io.emit('chat message', msg);
    });

    socket.on('disconnect', () => {
        console.log('Usuário desconectado');
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
