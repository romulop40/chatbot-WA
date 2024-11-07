# vector_db.py

#Codigo Vetor com problema
#import os
#import pinecone

#class VectorDB:
#    def __init__(self):
        # Conecta ao Pinecone usando a chave da API
#        pinecone.init(api_key=os.getenv("PINECONE_API_KEY"))
#        self.index = pinecone.Index("chatbot_memory")

#    def store(self, query, response):
        # Armazena o vetor do dado relevante
#        self.index.upsert([{"id": query, "values": response}])

#    def search(self, query):
        # Recupera dados com base em similaridade de vetor
#        return self.index.query([query], top_k=1)

#-------------------------------------------------------

#Codigo Vetor com problema
#import os
#from pinecone import Pinecone, Index, ServerlessSpec

#class VectorDB:
#    def __init__(self):
#        # Aqui cria uma instância do Pinecone usando a chave da API
#        self.pinecone_client = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        
        # Define o nome do índice
#        index_name = "chatbot-memory"  # Atualizado para "chatbot-memory" conforme ajuste

        # Verifica se o índice já existe, se não, cria um novo índice
#        if index_name not in self.pinecone_client.list_indexes():
#            self.pinecone_client.create_index(
#                name=index_name,
#                dimension=1024,  # Ajuste a dimensão conforme necessário
#                metric="cosine",
#                spec=ServerlessSpec(cloud="aws", region="us-east-1")  # Ajuste a região conforme necessário
#            )
        
        # Conecta ao índice existente usando a classe Index
#        self.index = Index(index_name)

#    def store(self, query, response):
        # Armazena o vetor do dado relevante
#        self.index.upsert([{"id": query, "values": response}])

#    def search(self, query):
        # Recupera dados com base em similaridade de vetor
#        return self.index.query([query], top_k=1)

#---------------------------------------------------------------

#- Teste vetor criando do zero, com novo indice no site pinecode
import os
from pinecone import Pinecone, ServerlessSpec, Index

class VectorDB:
    def __init__(self):
        # Aqui cria uma instância do Pinecone usando a chave da API
        self.pinecone_client = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        
        # Nome do índice
        index_name = "multilingual-e5-large"  # Escolha um nome único ou verifique o nome desejado

        # Aqui verifica se o índice já existe
        if index_name not in self.pinecone_client.list_indexes().names():
            print(f"Índice '{index_name}' não encontrado. Criando novo índice...")
            # Logo cria um novo índice com especificações definidas
            self.pinecone_client.create_index(
                name=index_name,
                dimension=1024,  # Número de dimensões do vetor
                metric="cosine",  # Métrica de similaridade
                spec=ServerlessSpec(cloud="aws", region="us-east-1")  # Configuração do servidor
            )
            print(f"Índice '{index_name}' criado com sucesso!")

        # OBS Rômulo, URL do host do índice (pego do painel do Pinecone do meu perfil Rômulo)
        host = "https://multilingual-e5-large-ws83ipf.svc.aped-4627-b74a.pinecone.io"
        
        # Conecta ao índice existente ou recém-criado
        self.index = Index(index_name, host=host)

    def store(self, query, response):
        # Armazena o vetor do dado relevante
        self.index.upsert([{"id": query, "values": response}])

    def search(self, query):
        # Recupera dados com base em similaridade de vetor
        return self.index.query([query], top_k=1)



