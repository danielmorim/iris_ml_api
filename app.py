from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import joblib
import numpy as np
import pandas as pd
import os
from pipeline import run_pipeline
from docs import swaggerui_blueprint, SWAGGER_URL
from config import MODEL_FILENAME, SCALER_FILENAME

app = Flask(__name__)
api = Api(app)

# Verificar se os modelos já existem; se não, treinar
if not os.path.exists(MODEL_FILENAME) or not os.path.exists(SCALER_FILENAME):
    print("Modelo não encontrado. Reproduzindo a pipeline...")
    run_pipeline()
else:
    print("Modelo encontrado. Iniciando a API...")

# Carregar o modelo e o scaler treinados
model = joblib.load(MODEL_FILENAME)
scaler = joblib.load(SCALER_FILENAME)

class Predict(Resource):
    def get(self):
        # Mapeando os parâmetros da query string com seus nomes
        params = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    
        print('Verificando os dados recebidos')
        try:
            # Extraindo os parâmetros e convertendo-os para float
            values = [float(request.args.get(param)) for param in params]
        except (TypeError, ValueError):
            return {"error": "Parâmetros inválidos"}, 400

        # Criar o DataFrame diretamente a partir dos valores recebidos
        features = pd.DataFrame([values], columns=np.char.replace(np.array(params), '_', ' '))
        
        # Escalar os dados
        print('Escalando os dados')
        features_scaled = scaler.transform(features)
        
        # Fazer a previsão
        print('Fazendo a previsão')
        prediction = model.predict(features_scaled)
        
        # Retornar a previsão como resposta JSON
        print('Retornando a resposta')
        return jsonify({'specie': prediction[0]})

api.add_resource(Predict, '/predict')
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    print('Iniciando a API...')
    app.run(host='0.0.0.0', port=5000)