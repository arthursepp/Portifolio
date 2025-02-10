import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from leitor import *

app = Flask(__name__)
CORS(app)  # Permite requisições de outras origens

@app.route('/carregar-documento', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'erro': 'Nenhum arquivo foi enviado'}), 400   
    
    arquivo = request.files['file']
    caminho = f"static/{arquivo.filename}"
    arquivo.save(caminho)  # Salvando localmente o PDF

    # Verifica se os itens foram enviados corretamente
    itens_body = request.form.get("itens")
    if not itens_body:
        return jsonify({'erro': 'Nenhum item foi enviado.'}), 400

    try:
        itens = json.loads(itens_body)  # Converte string JSON em lista de dicionários
        if not isinstance(itens, list):
            raise ValueError("Os itens devem ser uma lista.")
    except (json.JSONDecodeError, ValueError) as e:
        return jsonify({'erro': f'Erro ao processar os itens: {str(e)}'}), 400

    # Verifica se o PDF contém imagens e extrai o texto
    img_t_f = tem_imagem(caminho)
    texto_extraido = leitor_imagem(caminho) if img_t_f else leitor_texto(caminho)
    texto_extraido = texto_extraido.lower().strip() if isinstance(texto_extraido, str) else ""

    # Converte os termos em minúsculas para um conjunto para busca rápida
    termos_busca = {item['termo'].lower() for item in itens if 'termo' in item}

    # Atualiza os itens se forem encontrados no texto
    for item in itens:
        if 'termo' in item:
            item['encontrado'] = item['termo'].lower() in texto_extraido

    return jsonify({
        'mensagem': 'Arquivo processado com sucesso',
        'tem_imagem': img_t_f,
        'itens': itens  # Lista de termos atualizada
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
