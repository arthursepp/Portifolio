# Leitor de PDF Python combinado com Node.js

# Sinopse da Aplicação

Esta aplicação permite ao usuário fazer upload de arquivos PDF e buscar termos específicos dentro desses documentos. A funcionalidade principal consiste em carregar um PDF, analisar se o documento contém imagens ou texto, e então realizar a busca de termos fornecidos pelo usuário.

## Funcionalidades Principais:
- **Envio de Arquivo**: O usuário pode enviar um arquivo PDF para a aplicação.
- **Busca de Termos**: O usuário insere uma lista de termos para serem procurados dentro do conteúdo do PDF.
- **Leitura de Documentos**: O sistema pode analisar documentos que contenham texto ou imagens:
  - **Texto**: Se o PDF contiver apenas texto, ele será extraído e analisado.
  - **Imagens**: Se o PDF contiver imagens, o texto será extraído utilizando OCR (Tesseract).
- **Resultado**: O sistema retornará os termos encontrados ou não encontrados, além de mostrar o texto extraído ou as imagens do PDF.

## Tecnologias Utilizadas:
- **Frontend**: React
- **Backend**: Flask
- **OCR**: Tesseract para extração de texto de imagens
- **Bibliotecas**: 
  - `axios` para comunicação entre frontend e backend
  - `pytesseract` para OCR em imagens
  - `PyMuPDF (fitz)` para manipulação de PDFs

## Como Funciona:
1. O usuário envia um arquivo PDF.
2. Os termos de busca são informados.
3. A aplicação analisa o PDF, detecta imagens e extrai o texto.
4. O sistema verifica se os termos informados pelo usuário estão presentes no conteúdo extraído do PDF.
5. O resultado é retornado ao usuário, mostrando quais termos foram encontrados e em quais partes do documento.

## Instalação e Execução:
### Backend (Flask)
1. Instale as dependências:

    - **API:**
      - Caminhe até o diretório da api e execute o seguinte comando:
        ```bash
        pip install -r requirements.txt

    - **Servidor Node:**
      - Caminhe até o diretório do servidor e execute o seguinte comando:
        ```bash
        npm install
    
    - **Frontend React:**
      - Caminhar até o diretório do frontend e executar o mesmo comando do servidor node.


2. Executar a aplicação:

    Abra 3 terminais: Um para a API, um para o servidor node e um para a aplicação react.
- **Executando a API**
  ```bash
  python server.py
- **Executando o servidor node**
    ```bash
    npm start
**Execute o mesmo comando para rodar o frontend.**   