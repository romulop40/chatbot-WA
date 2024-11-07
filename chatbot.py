# chatbot.py
# Chatbot funcional, esta funcionando, vou incrementar uma chama no open no codigo abaixo
#import os
#from langchain.llms import OpenAI  # Importa o modelo OpenAI da biblioteca langchain
#from langchain.memory import ConversationBufferMemory  # Importa o gerenciador de memória
#from vector_db import VectorDB  # Certifique-se de que esse módulo existe e está correto

#class Chatbot:
#    def __init__(self):
        # Inicializa o modelo de linguagem com a chave da API
#        self.llm = OpenAI(api_key=os.getenv("LLM_API_KEY"))  
#        self.memory = ConversationBufferMemory()  # Gerencia memória para preferências
#        self.db = VectorDB()  # Conexão com o banco de dados vetorial

#    def respond(self, user_input):
        # Gera uma resposta usando o modelo de linguagem
#        response = self.llm(user_input)  
        
        # Verifica se há preferências ou fatos relevantes
#        if self.is_valid_information(response):
#            self.db.store(user_input, response)  # Armazena a interação no banco de dados
#        return response
    
#    def is_valid_information(self, response):
        # Implementa uma verificação para aceitar apenas dados válidos
#        return "preferência" in response  # Modifique a lógica conforme necessário

#--------------------------------------------------

#Chamada no codigo novo com o open ai, limite de chamada da API

#import os
#import time
#from langchain.llms import OpenAI  # Importa o modelo OpenAI da biblioteca langchain
#from langchain.memory import ConversationBufferMemory  # Importa o gerenciador de memória
#import openai  # Biblioteca OpenAI
#from vector_db import VectorDB  # Certifique-se de que esse módulo existe e está correto

#class Chatbot:
#    def __init__(self):
        # Inicializa o modelo de linguagem com a chave da API
#        self.llm = OpenAI(api_key=os.getenv("LLM_API_KEY"))  
#        self.memory = ConversationBufferMemory()  # Gerencia memória para preferências
#        self.db = VectorDB()  # Conexão com o banco de dados vetorial

#    def call_openai_api(self, prompt):
#        retries = 3
#        for _ in range(retries):
#            try:
                # Chama a API OpenAI
#                response = self.llm(prompt)
#                return response
#            except openai.OpenAIError as e:  # Captura qualquer erro da API OpenAI
                # Verifica se o erro é de rate limit
#                if 'RateLimitError' in str(e):  
#                    print("Rate limit excedido, tentando novamente...")
#                    time.sleep(60)  # Espera 60 segundos antes de tentar novamente
#                else:
#                    raise e  # Relança qualquer outro erro
#        raise Exception("Limite de requisições excedido após tentativas")

#    def respond(self, user_input):
        # Usa a função com retry para chamar o modelo de linguagem
#        response = self.call_openai_api(user_input)  
        
        # Verifica se há preferências ou fatos relevantes
#        if self.is_valid_information(response):
#            self.db.store(user_input, response)  # Armazena a interação no banco de dados
#        return response
    
#    def is_valid_information(self, response):
        # Implementa uma verificação para aceitar apenas dados válidos
#        return "preferência" in response  # Modifique a lógica conforme necessário


#------------------------------------------------------------------------
#Novo teste do chat pois o Open ai esta cobrando
#Dialogflow da Google

#Biblioteca:

#pip install google-cloud-dialogflow
#pip install --upgrade langchain


import os
from google.cloud import dialogflow_v2 as dialogflow
from langchain.memory import ConversationBufferMemory
from vector_db import VectorDB

class Chatbot:
    def __init__(self):
        # Campos de definir as credenciais para o Google Cloud Dialogflow
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/app/config/ferrous-griffin-440920-b5-8b07bd92aa79.json"
        
        # Configuração para o cliente do Dialogflow
        self.session_client = dialogflow.SessionsClient()
        self.language_code = 'pt-BR'  # Idioma (português, por exemplo)
        
        # Configuração da memória conforme requisitos mais recentes
        self.memory = ConversationBufferMemory(return_messages=True)#OBS Rômulo, Creio que os argumentos esteja corretos, implementar mais

        self.db = VectorDB()  # Aqui é a conexão com o banco de dados vetorial

    def detect_intent_texts(self, project_id, session_id, text):
        session = self.session_client.session_path(project_id, session_id)
        text_input = dialogflow.TextInput(text=text, language_code=self.language_code)
        query_input = dialogflow.QueryInput(text=text_input)

        try:
            # Essa sessão envia a consulta para o Dialogflow
            response = self.session_client.detect_intent(request={"session": session, "query_input": query_input})
            return response.query_result.fulfillment_text
        except Exception as e:
            print(f"Erro ao se comunicar com o Dialogflow: {e}")
            return "Desculpe, houve um erro ao processar sua solicitação."

    def respond(self, user_input):
        project_id = 'dialogflow-service-account'  # Substitua pelo seu ID do Google Cloud
        session_id = '110669289705647362498'  # Um identificador único para a sessão

        # Envia o texto para o Dialogflow e recebe a resposta
        response = self.detect_intent_texts(project_id, session_id, user_input)

        # Aqui verifica se há informações são válidas e armazena a interação
        if self.is_valid_information(response):
            self.db.store(user_input, response)  # Campo que armazena a interação no banco de dados

        return response
    
    def is_valid_information(self, response):
        # Aqui implementa uma verificação para aceitar apenas dados válidos
        return "preferência" in response  # OBS Rômulo, preciso modificar mais a parte lógica

if __name__ == "__main__":
    chatbot = Chatbot()

    print("Chatbot está pronto! (Digite 'sair' para encerrar)")

    while True:
        user_input = input("Você: ")
        
        if user_input.lower() == 'sair':
            print("Bot: Até logo!")
            break
        
        # Recebe a resposta do chatbot
        response = chatbot.respond(user_input)
        print(f"Bot: {response}")
