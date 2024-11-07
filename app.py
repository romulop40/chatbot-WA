# app.py
#primeiro chat simples, para teste
#import streamlit as st
#from chatbot import Chatbot

#st.title("Chatbot WA")

# Inicializa o chatbot
#bot = Chatbot()

# Interface de entrada e exibição de respostas
#user_input = st.text_input("Digite sua mensagem:")
#if user_input:
#    response = bot.respond(user_input)
#    st.write(f"Chatbot: {response}")
    
    # Log de mensagens
#    if "histórico" not in st.session_state:
#        st.session_state["histórico"] = []
#    st.session_state["histórico"].append({"User": user_input, "Bot": response})
    
    # Exibe o histórico
#    st.write("Histórico:")
#    for chat in st.session_state["histórico"]:
#        st.write(f"{chat['User']} -> {chat['Bot']}")

#------------------------------------------------------------

#Pagina WEB do chatbot, Modifiquei o Layout para deixar mais interativo, logo o codigo a cima foi para teste

# app.py
import streamlit as st
from chatbot import Chatbot

# Título e descrição, informações na entrada da aplicação
st.title("Chatbot WA, Teste Rômulo")
st.markdown("Interaja com o chatbot e veja o histórico das conversas!")

# Aqui Inicializa o chatbot
bot = Chatbot()

# Esse campo de entrada de mensagem do usuário
user_input = st.text_input("Digite sua mensagem:", key="user_input")

# Processamento da mensagem quando o usuário digitar algo
if user_input:
    # Obter a resposta do chatbot
    response = bot.respond(user_input)
    st.write(f"**Chatbot:** {response}")

    # Inicializa o histórico se não existir
    if "histórico" not in st.session_state:
        st.session_state["histórico"] = []

    # Adiciona a conversa atual ao histórico
    st.session_state["histórico"].append({"User": user_input, "Bot": response})

    # Exibe o histórico de mensagens
    st.subheader("Histórico de Conversa:")
    for chat in st.session_state["histórico"]:
        st.markdown(f"**Você:** {chat['User']}")
        st.markdown(f"**Chatbot:** {chat['Bot']}")
        st.write("---")  # Linha separadora entre as mensagens
