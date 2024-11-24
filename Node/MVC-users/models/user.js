const users = [
    { nome: "Alice", email: "alice@example.com" },
    { nome: "Bob", email: "bob@example.com" },
    { nome: "Charlie", email: "charlie@example.com" },
    { nome: "David", email: "david@example.com" },
]

function addUser(nome, email) {
    const user = { nome, email }
    users.push(user)
    return user
}

function getUsers() {
    return users
}

module.exports = { 
    addUser,
    getUsers 
}
