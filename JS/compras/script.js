
document.addEventListener('DOMContentLoaded', function() {
    let precoInicial = 0.00
    document.getElementById('precoInicial').innerText = "R$ " +  precoInicial.toFixed(2)  
})

class Produto {
    constructor(nome, qtd, marca, preco) {
        this.nome = nome
        this.marca = marca
        this.qtd = qtd
        this.preco = preco
    }    
}

function listaDeCompras() {
    const nome = document.getElementById('nomeProduto')
    const qtd = document.getElementById('qtdProduto')
    const marca = document.getElementById('marcaProduto')
    const preco = document.getElementById('precoProduto')
    const addItem = document.getElementById('addItemModal')  
    const tabelaProdutos = document.getElementById('tabelaProdutos')

    var precoTotal = 0    

    let carrinho = []

    addItem.addEventListener('click', () => {        
        const precoValue = preco.value
        const precoFloat = parseFloat(precoValue)

        // Caso o preço não seja um número:
        if (
            isNaN(precoFloat) ||
            isNaN(parseFloat(qtd.value)) ||
            qtd.value < 1
        ) {
            alert('Algum(ns) do(s) valor(es) não é válido. Tente novamente.')
        } else { // Caso seja um número:

            //Esconde o modal
            document.getElementById('modal').style.display = 'none'

            //Adiciona o preço do produto adicionado ao total
            precoTotal += (precoFloat * qtd.value)
            //Formatação do preço total para exibir duas casas decimais:
            document.getElementById('precoInicial').innerText = "R$ " + precoTotal.toFixed(2)
            
            //Adicionando um novo objeto Produto ao array do carrinho:
            const novoProduto = new Produto(
                nome.value,
                qtd.value,
                marca.value,
                preco.value
            )            
            carrinho.push(novoProduto)
            
            // Zerando os valores:
            nome.value = ""
            qtd.value = 1            
            marca.value = ""
            preco.value = ""

            //Mostrando o carrinho no console:
            console.log(carrinho)

            //Listando os produtos do carrinho na página:
            const novaLinha = document.createElement('tr')
            novaLinha.classList = 'produto-item'

            novaLinha.innerHTML = `
                <td>${novoProduto.nome}</td>
                <td>${novoProduto.qtd}</td>
                <td>${novoProduto.marca}</td>
                <td>${novoProduto.preco}</td>

                <td class='actions'>
                    <button type='button' class='editar-produto'>
                        <i class='fa fa-pencil'></i>
                    </button>
                    <button type='button' class='deletar-produto'>
                        <i class='fa fa-trash'></i>
                    </button>                    
                </td>
            `
            tabelaProdutos.appendChild(novaLinha)
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