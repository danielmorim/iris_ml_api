import os

ML_FOLDER = 'ml'
MODEL_FILENAME = f'{ML_FOLDER}/iris_model.pkl'
SCALER_FILENAME = f'{ML_FOLDER}/iris_scaler.pkl'

if not os.path.exists(ML_FOLDER):
    os.makedirs(ML_FOLDER)  # Cria o diretório (e subdiretórios, se necessário)
    print(f"Pasta '{ML_FOLDER}' criada.")
else:
    print(f"Pasta '{ML_FOLDER}' já existe.")