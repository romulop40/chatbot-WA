Este projeto é um chatbot desenvolvido em Python, com integração ao Google Dialogflow ou OpenAI (ambas as opções estão disponíveis no arquivo chatbot.py). Ele utiliza um banco de dados vetorial (VectorDB) para armazenamento de interações e é hospedado via Docker.

Estrutura do Projeto
chatbot.py: Classe principal do chatbot, integrando o Google Dialogflow e oferecendo memória de conversação.
vector_db.py: Gerencia o banco de dados vetorial, permitindo o armazenamento e a consulta das interações.
app.py: Script de inicialização do chatbot, oferecendo uma interface pelo Streamlit.
docker-compose.yml: Configuração dos serviços e volumes Docker para o chatbot e outros componentes.
Dockerfile: Define a imagem Docker para o ambiente Python e suas dependências.
requirements.txt: Lista de dependências Python necessárias para o projeto.
.env: Arquivo para armazenar variáveis de ambiente, como credenciais e configurações sensíveis.
Configuração e Instalação
Antes de começar, instale o Git Bash (caso esteja no Windows) e navegue até a pasta do projeto. Siga os passos abaixo para configurar e rodar o chatbot:

1. Instalar Bibliotecas Necessárias
Instale as dependências do projeto com os seguintes comandos:

# Construa os serviços com as variáveis de ambiente
docker-compose --env-file .env build

# Instale as dependências Python
pip install -r requirements.txt

# Verifique a instalação do Langchain
pip show langchain

# Atualize as bibliotecas, se necessário
pip install --upgrade openai
pip install google-cloud-dialogflow
pip install --upgrade langchain

2. Build e Execução do Projeto com Docker
Certifique-se de que o Docker Desktop está instalado (testado na versão 4.35.1). Em seguida, construa e inicie o contêiner:

docker-compose up --build

3. Acessando a Interface
Após iniciar o contêiner, acesse a interface do chatbot no navegador usando o endereço:

http://localhost:8501

4. Verificação de Logs
Em caso de problemas, consulte os logs para diagnóstico:

docker-compose logs
