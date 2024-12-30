
document.addEventListener('DOMContentLoaded', function() {
    let precoInicial = 0.00
    document.getElementById('precoInicial').innerText = "R$ " +  precoInicial.toFixed(2)  
})

class Produto {
    constructor(nome, marca, preco) {
        this.nome = nome
        this.marca = marca
        this.preco = preco
    }    
}

function listaDeCompras() {
    const nome = document.getElementById('nomeProduto')
    const marca = document.getElementById('marcaProduto')
    const preco = document.getElementById('precoProduto')
    const addItem = document.getElementById('addItemModal')  
    const lista = document.getElementById('lista')  

    var precoTotal = 0    

    let carrinho = []

    addItem.addEventListener('click', () => {
        const precoValue = preco.value
        const precoFloat = parseFloat(precoValue)

        // Caso o preço não seja um número:
        if (isNaN(precoFloat)) {
            alert('O valor inserido no preço não é válido. Tente novamente.')
        } else { // Caso seja um número:

            //Esconde o modal
            document.getElementById('modal').style.display = 'none'

            //Adiciona o preço do produto adicionado ao total
            precoTotal += precoFloat
            //Formatação do preço total para exibir duas casas decimais:
            document.getElementById('precoInicial').innerText = "R$ " + precoTotal.toFixed(2)
            
            //Adicionando um novo objeto Produto ao array do carrinho:
            const novoProduto = new Produto(
                nome.value,
                marca.value,
                preco.value
            )            
            carrinho.push(novoProduto)
            
            // Zerando os valores:
            nome.value = ""
            marca.value = ""
            preco.value = ""            

            //Mostrando o carrinho no console:
            console.log(carrinho)

            //Listando os produtos do carrinho na página:
            const produtoHTML = document.createElement('div')
            produtoHTML.className = 'produto-item'
            produtoHTML.innerHTML = `
                <span>Nome: ${novoProduto.nome}</span>
                <span>Marca: ${novoProduto.marca}</span>
                <span>Preço: R$ ${novoProduto.preco}</span>
                <button type="button" class="editar-produto" id="editarProduto">
                    <i class="fa fa-pencil"></i>
                </button>
                <button type="button" class="deletar-produto" id="deletarProduto">
                    <i class="fa fa-trash"></i>
                </button>
            `
            lista.appendChild(produtoHTML)
        }
    })
}

function operateModal() {
    const open = document.getElementById('addItem')
    const close = document.getElementById('fecharModal')    

    open.addEventListener('click', () => {
        document.getElementById('modal').style.display = 'flex'
    })

    close.addEventListener('click', () => {
        document.getElementById('modal').style.display = 'none'
    })
}

operateModal()
listaDeCompras()