FROM python:3.9.18

WORKDIR /usr/src/app

# Copiar os arquivos necessários para o container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para iniciar a API
CMD [ "python", "./app.py" ]