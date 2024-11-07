# Dockerfile
#FROM python:3.9

#WORKDIR /app

# Instala as dependências
#COPY requirements.txt .
#RUN pip install -r requirements.txt

#COPY . /app

#CMD ["streamlit", "run", "app.py", "--server.port=8501"]

#Novo Dockerfile Atualizado para o projeto atual, logo o codigo acima foi para teste
# Usa uma imagem base do Python
FROM python:3.9

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# Copia o arquivo de credenciais (ajuste o caminho conforme seu projeto)
COPY ./config/ferrous-griffin-440920-b5-8b07bd92aa79.json /app/ferrous-griffin-440920-b5-8b07bd92aa79.json

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto para o contêiner
COPY . .

# Executa o aplicativo com Streamlit na porta especificada
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

