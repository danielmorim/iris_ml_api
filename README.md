# Iris Classification API

Este projeto implementa uma API para classificar flores do tipo Íris utilizando um modelo de Regressão Logística. A API é construída em Flask e utiliza o conjunto de dados Iris disponível no UCI Machine Learning Repository.

## Tecnologias Utilizadas

- Python
- Flask
- Flask-RESTful
- scikit-learn
- pandas
- joblib
- ucimlrepo
- Docker

## Estrutura do Projeto

```bash
iris_ml_api/
│
├── app.py               # Código da API
├── pipeline.py          # Código para treinamento do modelo
├── Dockerfile           # Arquivo de configuração do Docker
├── requirements.txt     # Dependências do projeto
├── iris_model.pkl       # Modelo treinado (gerado após a execução da pipeline)
└── iris_scaler.pkl      # Scaler treinado (gerado após a execução da pipeline)
```

## Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes do Python)
- Docker (para execução em container)

## Instalação

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd iris_ml_api
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Para Windows
   # source venv/bin/activate  # Para Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Reproduzir a pipeline
Para reproduzir a pipeline, treinar o modelo e gerar os arquivos iris_model.pkl e iris_scaler.pkl, execute:
    ```bash
   python pipeline.py
   ```
