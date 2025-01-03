
document.addEventListener('DOMContentLoaded', function() {
    let precoInicial = 0.00
    document.getElementById('precoInicial').innerText = "R$ " +  precoInicial.toFixed(2)  
})

class Produto {
    constructor(id, nome, qtd, marca, preco) {
        this.id = id
        this.nome = nome
        this.marca = marca
        this.qtd = qtd
        this.preco = preco
    }    
}

function listaDeCompras() {
    let id = 1
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
            isNaN(parseInt(qtd.value)) ||
            qtd.value < 1
        ) {
            alert('Alguns dos valores são inválidos. Tente novamente.')
        } else if (!nome.value.trim()){ // Caso o campo do nome esteja vazio
            alert('Insira um nome')
        }        
        else { // Caso seja um número:

            //Esconde o modal
            document.getElementById('modal').style.display = 'none'                      
            
            //Adicionando um novo objeto Produto ao array do carrinho:
            const novoProduto = new Produto(
                Date.now(),                
                nome.value,
                parseInt(qtd.value),
                marca.value,
                preco.value
            )            
            carrinho.push(novoProduto)        

            //Mostrando o carrinho no console:
            console.log(carrinho)

            precoTotal += novoProduto.preco * novoProduto.qtd
            //Formatação do preço total para exibir duas casas decimais:
            document.getElementById('precoInicial').innerText = "R$ " + precoTotal.toFixed(2)
            
            // Zerando os valores:
            nome.value = ""
            qtd.value = 1            
            marca.value = ""
            preco.value = ""            

            //Listando os produtos do carrinho na página:
            const novaLinha = document.createElement('tr')
            novaLinha.classList = 'produto-item'
            novaLinha.dataset.id = novoProduto.id

            novaLinha.innerHTML = `
                <td>${novoProduto.nome}</td>
                <td>${novoProduto.qtd}</td>
                <td>${novoProduto.marca}</td>
                <td>${novoProduto.preco}</td>

                <td class='actions'>
                    <button type='button' id='deletar' class='editar-produto'>
                        <i class='fa fa-pencil'></i>
                    </button>
                    <button type='button' id='editar' class='deletar-produto'>
                        <i class='fa fa-trash'></i>
                    </button>                    
                </td>
            `
            tabelaProdutos.appendChild(novaLinha)            

            novaLinha.querySelector('.deletar-produto').addEventListener('click', () => {
                deletarProduto(novoProduto.id)
            })
        }
    })

    function deletarProduto(id) {
        carrinho = carrinho.filter(produto => produto.id !== id)

        precoTotal = carrinho.reduce((total, produto) => total + produto.preco * produto.qtd, 0)
        document.getElementById('precoInicial').innerText = 'R$ ' + precoTotal.toFixed(2)

        const linha = document.querySelector(`tr[data-id="${id}"]`)
        if (linha) linha.remove()

        console.log("Produto removido:", id)
        console.log("Carrinho atualizado:", carrinho)
    }

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