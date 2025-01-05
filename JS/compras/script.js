// Definindo informações assim que a página é carregada:
document.addEventListener("DOMContentLoaded", function () {
    let precoInicial = 0.0; // Valor inicial do preço total
    document.getElementById("precoInicial").innerText = "R$ " + precoInicial.toFixed(2); // Formatando o preço total
});

// Construindo o produto
class Produto {
    constructor(id, nome, qtd, marca, preco) {
        this.id = id; // ID único do produto
        this.nome = nome; // Nome do produto
        this.qtd = qtd; // Quantidade do produto
        this.marca = marca; // Marca do produto
        this.preco = preco; // Preço do produto
    }
}

// Função da lista de compras
function listaDeCompras() {
    // Obtendo referências aos elementos HTML:
    const nome = document.getElementById("nomeProduto");
    const qtd = document.getElementById("qtdProduto");
    const marca = document.getElementById("marcaProduto");
    const preco = document.getElementById("precoProduto");
    const addItem = document.getElementById("addItemModal");
    const tabelaProdutos = document.getElementById("tabelaProdutos");

    let precoTotal = 0; // Variável para armazenar o preço total
    let carrinho = []; // Lista de produtos no carrinho
    let produtoEditando = null; // Produto que está sendo editado (se houver)

    // Adicionar produto à lista ou atualizar um existente
    addItem.addEventListener("click", () => {
        const precoValue = parseFloat(preco.value); // Converte o valor do preço para número
        const qtdValue = parseInt(qtd.value); // Converte a quantidade para número inteiro

        // Validações dos campos
        if (
            isNaN(precoValue) ||
            isNaN(qtdValue) ||
            qtdValue < 1 ||
            !nome.value.trim()
        ) {
            alert("Preencha os campos corretamente."); // Alerta se os campos não estiverem válidos
        } else {
            if (produtoEditando) {
                // Atualiza os dados do produto em edição
                produtoEditando.nome = nome.value.trim();
                produtoEditando.qtd = qtdValue;
                produtoEditando.marca = marca.value.trim();
                produtoEditando.preco = precoValue;
                atualizarTabela();
                produtoEditando = null; // Limpa o status de edição para editar novamente, se necessário.
            } else {
                // Criando um novo produto:
                const novoProduto = new Produto(
                    Date.now(),
                    nome.value.trim(),
                    qtdValue,
                    marca.value.trim(),
                    precoValue
                );
                carrinho.push(novoProduto); // Adiciona o novo produto à lista
                precoTotal += novoProduto.preco * novoProduto.qtd; // Atualiza o preço total
                adicionarLinhaTabela(novoProduto); // Adiciona o produto à tabela
            }

            // Limpando os campos do modal
            nome.value = "";
            qtd.value = 1;
            marca.value = "";
            preco.value = "";

            // Atualiza o preço total exibido na página
            atualizarPrecoTotal()          
            fecharModal(); // Fecha o modal
        }
    });

    // Atualiza o preco total (Em uma função por ser usado múltiplas vezes.)
    function atualizarPrecoTotal() {
        precoTotal = carrinho.reduce((total, produto) => total + produto.preco * produto.qtd, 0);
        document.getElementById("precoInicial").innerText = "R$ " + precoTotal.toFixed(2);            
    }

    // Adiciona o novo produto, com suas informações, à tabela:
    function adicionarLinhaTabela(produto) {
        const novaLinha = document.createElement("tr"); // Criando uma nova linha na tabela para o produto
        novaLinha.classList.add("produto-item"); // Adicionando a classe 'produto-item' à nova linha.
        novaLinha.dataset.id = produto.id; // Define o ID do produto como atributo data-id

        // Conteúdo da nova linha:
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

        // Editar o produto ao clicar no botão de edição
        novaLinha.querySelector(".editar-produto").addEventListener("click", () => {
            // Chamando a função de editar o produto e passando para ela o produto a ser editado
            editarProduto(produto.id);
        });

        // Deletar o produto ao clicar no botão de exclusão
        novaLinha.querySelector(".deletar-produto").addEventListener("click", () => {
            // Chamando a função de deletar o produto e passando para ela o produto a ser deletado
            deletarProduto(produto.id);
        });

        tabelaProdutos.appendChild(novaLinha); // Adiciona a nova linha à tabela
    }

    // Função para deletar um produto do carrinho
    function deletarProduto(id) {
        carrinho = carrinho.filter((produto) => produto.id !== id); // Remove o produto pelo ID
        atualizarTabela(); // Atualiza a tabela para refletir a exclusão
        atualizarPrecoTotal(); // Atualiza o preço total
    }

    // Função para editar um produto
    function editarProduto(id) {
        const produto = carrinho.find((p) => p.id === id); // Encontra o produto pelo ID
        if (!produto) return alert("Produto não encontrado."); // Exibe erro se o produto não existir

        // Preenche os campos do modal com os dados do produto
        produtoEditando = produto;
        nome.value = produto.nome;
        qtd.value = produto.qtd;
        marca.value = produto.marca;
        preco.value = produto.preco;

        abrirModal(); // Abre o modal para edição
    }

    // Atualizando a tabela
    function atualizarTabela() {
        tabelaProdutos.innerHTML = ""; // Limpa o conteúdo da tabela
        carrinho.forEach((produto) => adicionarLinhaTabela(produto)); // Recria a tabela com os produtos do carrinho
    }

    // Operando o modal:
    function abrirModal() {
        document.getElementById("modal").style.display = "block";
        document.getElementById("containerModal").style.display = "flex";
    }

    function fecharModal() {
        document.getElementById("modal").style.display = "none";
        document.getElementById("containerModal").style.display = "none";
    }
}

// Função para operar o modal (abrir/fechar)
function operateModal() {
    const open = document.getElementById("addItem");
    const close = document.getElementById("fecharModal");

    // Evento para abrir o modal
    open.addEventListener("click", () => {
        document.getElementById("modal").style.display = "block";
        document.getElementById("containerModal").style.display = "flex";
    });

    // Evento para fechar o modal
    close.addEventListener("click", () => {
        document.getElementById("modal").style.display = "none";
        document.getElementById("containerModal").style.display = "none";
    });
}

// Inicializa o modal e a lista de compras
operateModal();
listaDeCompras();
