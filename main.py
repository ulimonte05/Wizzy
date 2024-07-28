import streamlit as st
import os
from streamlit_chat import message
from services.ai import AIAssistant
from services.products import ProductInventory
from services.forms import show_inventory

# Instancias de las clases
products_manager = ProductInventory(os.path.join(os.path.dirname(__file__), "db/ecommerce_inventory.csv"))
ai_assistant = AIAssistant(os.path.join(os.path.dirname(__file__), "db/ecommerce_inventory.csv"), os.getenv('API_KEY'))

# Inicializar el historial de la conversación
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = ""

# Manejo del input del usuario
def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    
    # Generar la respuesta y actualizar el historial de la conversación
    response, st.session_state.conversation_history = ai_assistant.generate_response(user_input)
    
    st.session_state.generated.append(response)
    st.session_state.user_input = ""  # Vaciar el input de envío

# Reiniciar el historial de la conversación
def on_btn_click():
    st.session_state.past.clear()
    st.session_state.generated.clear()
    st.session_state.conversation_history = ""

# Inicializar estado de la sesión
st.session_state.setdefault("past", [])
st.session_state.setdefault("generated", [])

# Título de la aplicación
st.title("Wizzy")

# Selección de sección en la barra lateral
section = st.sidebar.selectbox("Seleccionar sección", ["Chat", "Inventario"])

# Mostrar sección seleccionada
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
    show_inventory(products_manager)
