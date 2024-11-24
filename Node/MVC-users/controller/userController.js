const userModel = require('../models/user.js');

function renderUsers(req, res) {
    const users = userModel.getUsers();
    res.render('lista', { users });
}

module.exports = {
    renderUsers
}
