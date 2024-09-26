# Iris Classification API

Este projeto implementa uma API para classificar flores do tipo Íris utilizando um modelo de Regressão Logística. A API é construída em Flask e utiliza o conjunto de dados Iris disponível no [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/53/iris).

## Principais Tecnologias Utilizadas

- Python
- Flask
- scikit-learn
- joblib
- Docker

## Estrutura do Projeto

```bash
iris_ml_api/
│
├── static/              # Diretório para arquivos estáticos
│   └── swagger.json     # Configuração da documentação da API no Swagger
├── app.py               # Código da API
├── config.py            # Configuração com o nome dos arquivos do modelo e pasta de armazenamento
├── Dockerfile           # Arquivo de configuração do Docker
├── docs.py              # Configuração do Swagger para documentação da API
├── pipeline.py          # Código para treinamento do modelo
└── requirements.txt     # Dependências do projeto
```

## Pré-requisitos

- Docker (para execução em container)

## Instruções de Uso

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd iris_ml_api
   ```

2. Faça o build da imagem Docker:
   ```bash
   docker build -t iris_api:latest .
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Reproduzir a pipeline

Para reproduzir a pipeline, treinar o modelo e gerar os arquivos `iris_model.pkl` e `iris_scaler.pkl`, execute (Windows):
   ```bash
   docker run -it -v ${PWD}/ml:/usr/src/app/ml/ iris_api:latest pipeline.py
   ```
Isso monta o diretório atual (`${PWD}/ml`) no diretório `/usr/src/app/ml/` dentro do container, permitindo que os arquivos gerados sejam acessíveis fora do container.

## Iniciar a API

Para iniciar a API, execute:
   ```bash
   docker run -it -p 5000:5000 iris_api:latest python app.py
   ```
A API estará disponível em http://localhost:5000/.

## Documentação da API

A documentação da API no Swagger está disponível na raiz (/): http://localhost:5000/


## Endpoints

- /predict: Endpoint para previsão da espécie de íris com base nas características fornecidas.

### Parâmetros

- `sepal_length`: Comprimento da sépala (float)
- `sepal_width`: Largura da sépala (float)
- `petal_length`: Comprimento da pétala (float)
- `petal_width`: Largura da pétala (float)

### Exemplos de Uso

#### Iris Setosa:
```text
/predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2
```
Resposta esperada: `{"specie": "Iris-setosa"}`

#### Iris Versicolor:
```text
/predict?sepal_length=6.4&sepal_width=3.2&petal_length=4.5&petal_width=1.5
```
Resposta esperada: `{"specie": "Iris-versicolor"}`

#### Iris Virginica:
```text
/predict?sepal_length=5.8&sepal_width=3.1&petal_length=5.1&petal_width=1.9
```
Resposta esperada: `{"specie": "Iris-virginica"}`

## Considerações Finais

Essa versão do README.md assume que o projeto será executado inteiramente dentro de containers Docker, simplificando a instalação e configuração do ambiente. As instruções de uso fornecem os comandos necessários para construir a imagem, executar a pipeline de treinamento e iniciar a API. Além disso, são fornecidos exemplos de uso da API para classificação das três espécies de íris, incluindo detalhes sobre os parâmetros necessários para as requisições ao endpoint /predict.