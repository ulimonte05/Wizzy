import streamlit as st
import os
from streamlit_chat import message
from service.pandasai import generateResponse
import pandas as pd
import google.generativeai as genai

# Configurar Google Generative AI con la clave API
genai.configure(api_key=os.getenv('API_KEY'))

# Cargar el archivo CSV de inventario
df = pd.read_csv("./db/ecommerce_inventory.csv")

# Inicializar el historial de la conversación
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = ""

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    
    # Generar la respuesta y actualizar el historial de la conversación
    response, st.session_state.conversation_history = generateResponse(
        user_input, st.session_state.conversation_history
    )
    
    st.session_state.generated.append(response)

def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]
    st.session_state.conversation_history = ""  # Reiniciar el historial de la conversación

def show_inventory():
    st.header("Inventario")
    st.dataframe(df)

st.session_state.setdefault("past", [])
st.session_state.setdefault("generated", [])

st.title("Wizzy")

# Agregar la selección de sección en la barra lateral
section = st.sidebar.selectbox("Seleccionar sección", ["Chat", "Inventario"])

if section == "Chat":
    chat_placeholder = st.empty()

    with chat_placeholder.container():
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
            message(st.session_state['generated'][i], key=f"{i}")

        st.button("Clear message", on_click=on_btn_click)

    with st.container():
        st.text_input("User Input:", on_change=on_input_change, key="user_input")
elif section == "Inventario":
    show_inventory()
