from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/gerar-imagem', methods=['POST'])
def gerar_imagem():
    data = request.get_json()
    tipo_cenario = data.get("tipoCenario", "residencial")
    tipo_formato = data.get("tipoFormato", "wide")
    incluir_modelos = data.get("incluirModelos", False)
    pratos = data.get("pratos", [])

    imagem_url = f"https://dummyimage.com/1500x800/cccccc/000000&text={tipo_cenario}+{tipo_formato}".replace(' ', '+')

    return jsonify({
        "imagem_url": imagem_url,
        "descricao": f"Imagem simulada para {tipo_cenario} em formato {tipo_formato}.",
        "nutrientes": pratos
    })

@app.route('/listar-cenarios', methods=['GET'])
def listar_cenarios():
    return jsonify({
        "cenarios": ["residencial", "restaurante_luxo", "self_service", "fast_food"]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
