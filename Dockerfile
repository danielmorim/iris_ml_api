FROM python:3.9.18

WORKDIR /usr/src/app

# Copiar os arquivos necessários para o container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expor a porta 5000 para acessar o Flask
EXPOSE 5000

# Comando para iniciar a API
ENTRYPOINT ["python"]
CMD ["app.py"]