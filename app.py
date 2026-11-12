from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

clasificador = pipeline(
    "sentiment-analysis",
    model="./modelo/trainer_model",      
    tokenizer="./modelo/trainer_model"   
)

def analizar_resena_con_ia(texto):
    try:
        resultado = clasificador(texto)[0]
        label_original = resultado['label']
        confianza = resultado['score']

        sentimiento = "POSITIVE" if label_original == "LABEL_1" else "NEGATIVE"
        return sentimiento, confianza

    except Exception as e:
        return f"Error al analizar: {e}", 0.0

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/analizar', methods=['POST'])
def analizar():
    data = request.json
    texto_usuario = data.get('resena', '')

    if not texto_usuario:
        return jsonify({"error": "No hay texto"}), 400

    etiqueta, confianza = analizar_resena_con_ia(texto_usuario)

    if etiqueta == "POSITIVE":
        respuesta = {
            "mensaje": f"¡Qué maravilla! Mi IA detecta que todo fue genial. ({int(confianza*100)}% de confianza)",
            "clase": "positivo"
        }
    else:
        respuesta = {
            "mensaje": f"Vaya, he detectado algo de negatividad... ({int(confianza*100)}% de sinceridad)",
            "clase": "negativo"
        }

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)