from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import joblib
import numpy as np
import os
from pipeline import run_pipeline

app = Flask(__name__)
api = Api(app)

MODEL_FILENAME = 'iris_model.pkl'
SCALER_FILENAME = 'iris_scaler.pkl'

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
    def post(self):
        data = request.get_json(force=True)
        sepal_length = data['sepal_length']
        sepal_width = data['sepal_width']
        petal_length = data['petal_length']
        petal_width = data['petal_width']
        
        # Criar array com as características da flor
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        
        # Escalar os dados
        features_scaled = scaler.transform(features)
        
        # Fazer a previsão
        prediction = model.predict(features_scaled)
        
        # Retornar a previsão como resposta JSON
        return jsonify({'species': prediction[0]})

api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run()