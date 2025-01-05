document.addEventListener("DOMContentLoaded", function () {
    let precoInicial = 0.0;
    document.getElementById("precoInicial").innerText = "R$ " + precoInicial.toFixed(2);
});

class Produto {
    constructor(id, nome, qtd, marca, preco) {
        this.id = id;
        this.nome = nome;
        this.qtd = qtd;
        this.marca = marca;
        this.preco = preco;
    }
}

function listaDeCompras() {
    const nome = document.getElementById("nomeProduto");
    const qtd = document.getElementById("qtdProduto");
    const marca = document.getElementById("marcaProduto");
    const preco = document.getElementById("precoProduto");
    const addItem = document.getElementById("addItemModal");
    const tabelaProdutos = document.getElementById("tabelaProdutos");

    let precoTotal = 0;
    let carrinho = [];
    let produtoEditando = null;

    // Adicionar produto
    addItem.addEventListener("click", () => {
        const precoValue = parseFloat(preco.value);
        const qtdValue = parseInt(qtd.value);

        if (
            isNaN(precoValue) ||
            isNaN(qtdValue) ||
            qtdValue < 1 ||
            !nome.value.trim()
        ) {
            alert("Preencha os campos corretamente.");
        } else {
            if (produtoEditando) {
                produtoEditando.nome = nome.value.trim();
                produtoEditando.qtd = qtdValue;
                produtoEditando.marca = marca.value.trim();
                produtoEditando.preco = precoValue;
                atualizarTabela();
                produtoEditando = null;
            } else {
                const novoProduto = new Produto(
                    Date.now(),
                    nome.value.trim(),
                    qtdValue,
                    marca.value.trim(),
                    precoValue
                );
                carrinho.push(novoProduto);
                precoTotal += novoProduto.preco * novoProduto.qtd;
                adicionarLinhaTabela(novoProduto);
            }

            atualizarPrecoTotal();
            limparCampos();
            fecharModal();
        }
    });

    // Função para atualizar preço total
    function atualizarPrecoTotal() {
        precoTotal = carrinho.reduce((total, produto) => total + produto.preco * produto.qtd, 0);
        document.getElementById("precoInicial").innerText = "R$ " + precoTotal.toFixed(2);
    }

    // Função para limpar os campos
    function limparCampos() {
        nome.value = "";
        qtd.value = 1;
        marca.value = "";
        preco.value = "";
    }

    // Função para adicionar uma linha na tabela
    function adicionarLinhaTabela(produto) {
        const novaLinha = document.createElement("tr");
        novaLinha.classList.add("produto-item");
        novaLinha.dataset.id = produto.id;

        novaLinha.innerHTML = `
            <td>${produto.nome}</td>
            <td>${produto.qtd}</td>
            <td>${produto.marca}</td>
            <td>R$ ${produto.preco.toFixed(2)}</td>
            <td class="actions">
                <button type="button" class="editar-produto">
                    <i class="fa fa-pencil"></i>
                </button>
                <button type="button" class="deletar-produto">
                    <i class="fa fa-trash"></i>
                </button>
            </td>
        `;

        novaLinha.querySelector(".editar-produto").addEventListener("click", () => {
            editarProduto(produto.id);
        });

        novaLinha.querySelector(".deletar-produto").addEventListener("click", () => {
            deletarProduto(produto.id);
        });

        tabelaProdutos.appendChild(novaLinha);
    }

    // Função para deletar produto
    function deletarProduto(id) {
        carrinho = carrinho.filter((produto) => produto.id !== id);
        atualizarTabela();
        atualizarPrecoTotal();
    }

    // Função para editar produto
    function editarProduto(id) {
        const produto = carrinho.find((p) => p.id === id);
        if (!produto) return alert("Produto não encontrado.");

        produtoEditando = produto;
        nome.value = produto.nome;
        qtd.value = produto.qtd;
        marca.value = produto.marca;
        preco.value = produto.preco;

        abrirModal();
    }

    // Atualizar a tabela
    function atualizarTabela() {
        tabelaProdutos.innerHTML = "";
        carrinho.forEach((produto) => adicionarLinhaTabela(produto));
    }

    // Modal control
    function abrirModal() {
        document.getElementById("modal").style.display = "block";
        document.getElementById("containerModal").style.display = "flex";
    }

    function fecharModal() {
        document.getElementById("modal").style.display = "none";
        document.getElementById("containerModal").style.display = "none";
    }
}

function operateModal() {
    const open = document.getElementById("addItem");
    const close = document.getElementById("fecharModal");

    open.addEventListener("click", () => {
        document.getElementById("modal").style.display = "block";
        document.getElementById("containerModal").style.display = "flex";
    });

    close.addEventListener("click", () => {
        document.getElementById("modal").style.display = "none";
        document.getElementById("containerModal").style.display = "none";
    });
}

operateModal();
listaDeCompras();
