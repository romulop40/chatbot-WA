Este projeto é um Chatbot desenvolvido em Python com integração ao Google Dialogflow ou OpenAI(OPÇÂO),tem as duas opções escrita no arquivo chatbot.py, 
utilizando um banco de dados vetorial (VectorDB) e hospedado via Docker. Abaixo estão as instruções de configuração e um resumo dos arquivos e bibliotecas envolvidos.

Estrutura do Projeto:

->chatbot.py: Classe principal do chatbot, que integra o Google Dialogflow e utiliza memória de conversação.
->vector_db.py: Script que gerencia o banco de dados vetorial para armazenamento e consulta das interações.
->app.py: Script de inicialização do chatbot com interface pelo Streamlit.
->docker-compose.yml: Configuração de serviços e volumes Docker para o chatbot e outros componentes.
->Dockerfile: Define a imagem Docker para o ambiente Python e as dependências.
->requirements.txt: Lista de dependências Python necessárias para o projeto.
->.env: Arquivo para armazenar variáveis de ambiente (como credenciais e configurações sensíveis).

Instalar o gitbash e abrir o caminho dentro da pasta do projeto e seguir os seguinte passos para rodar o chatbot:

#Bibliotecas para ser instalados:

==>#docker-compose --env-file .env build
==>#pip install -r requirements.txt
==>#pip show langchain
==>#pip install --upgrade openai
==>#pip install google-cloud-dialogflow
==>#pip install --upgrade langchain
==>#pip install google-cloud-dialogflow

Comando para Build do projeto, construir e iniciar o contêiner no Docker, versão usada Docker Desktop 4.35.1 (173168):

==>#docker-compose up --build

*Porta de acessar no navegador o projeto:

Localhost:8501

*Caso tenha problema, usar comando para ver os logs:
 
==>#docker-compose logs