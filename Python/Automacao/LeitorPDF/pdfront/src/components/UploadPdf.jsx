import React, { useState } from 'react'
import axios from 'axios'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faPlus, faUpload } from '@fortawesome/free-solid-svg-icons'

const UploadPdf = () => {
    const [file, setFile] = useState(null)
    const [mensagem, setMensagem] = useState("")
    const [items, setItems] = useState([])

    const handleFileChange = (event) => {
        setFile(event.target.files[0])
    }

    const addItensToArray = () => {
        const itemName = document.getElementById('itemName').value.trim()

        if (itemName !== "") {
            setItems(prevItems => [...prevItems, { termo: itemName, encontrado: false }])  // Adiciona novo termo
            document.getElementById('itemName').value = ""  // Limpa o input            
        } else {
            alert("Insira um termo válido!")
        }
    }

    const handleUpload = async () => {
        if (!file || items.length === 0) {
            alert('Selecione um arquivo e/ou informe termos que serão buscados!')
            return
        }

        const formData = new FormData()
        formData.append("file", file)
        formData.append("itens", JSON.stringify(items)) // Envia os termos como JSON

        try {
            const response = await axios.post("http://localhost:5000/carregar-documento", formData, {
                headers: { "Content-Type": "multipart/form-data" }
            })

            // Atualiza os itens com os valores retornados pela API
            setMensagem(response.data.mensagem)
            setItems(response.data.itens) // Atualiza o estado dos termos

        } catch (error) {
            setMensagem(`Erro ao enviar o arquivo: ${error.message}`)
        }
    }

    return (
        <div className="reader">
            <h3>Primeiro, digite as palavras que você deseja verificar se existem no texto do doc:</h3>
            <div className="itens-form">
                <div className="input-item-name">
                    <h4>Insira uma palavra:</h4>
                    <input type="text" id="itemName" />

                    <button id='newItem' onClick={addItensToArray}>
                        <FontAwesomeIcon icon={faPlus}></FontAwesomeIcon>
                        Adicionar
                    </button>
                </div>
                
                <div className="array-display">
                    <h4>Termos que serão buscados:</h4>
                    <ul>
                        {items.map((item, index) => (
                            <li key={index} style={{ color: item.encontrado ? "green" : "red" }}>
                                {item.termo} - Encontrado: {item.encontrado ? "✅ Sim" : "❌ Não"}
                            </li>
                        ))}
                    </ul>
                </div>
            </div>

            <div className="send-file">
                <h2>Enviar arquivo:</h2>
                <h4>Envie o arquivo em que as palavras da lista serão procuradas:</h4>
                <div className="input-field">
                    <input type="file" accept="application/pdf" onChange={handleFileChange} />
                    <button onClick={handleUpload}>
                        <FontAwesomeIcon icon={faUpload}></FontAwesomeIcon>
                        Enviar
                    </button>

                    {mensagem && <p>{mensagem}</p>}

                </div>
            </div>
        </div>
    )
}

export default UploadPdf
