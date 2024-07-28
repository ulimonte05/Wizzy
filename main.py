import streamlit as st
import os
from streamlit_chat import message
from service.ai import generateResponse
from service.products import ProductInventory
import pandas as pd
import google.generativeai as genai
products_manager = ProductInventory(os.path.join(os.path.dirname(__file__), "db/ecommerce_inventory.csv"))

# Configurar Google Generative AI con la clave API
genai.configure(api_key=os.getenv('API_KEY'))

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

    # Mostrar el inventario actual
    df = pd.DataFrame(products_manager.get_products())
    st.dataframe(df)
    
    st.subheader("Agregar Producto")
    with st.form("add_product_form"):
        ProductID = st.text_input("Product ID")
        ProductName = st.text_input("Product Name")
        Category = st.text_input("Category")
        Brand = st.text_input("Brand")
        Model = st.text_input("Model")
        Price = st.number_input("Price", min_value=0.0, format="%.2f")
        StockQuantity = st.number_input("Stock Quantity", min_value=0)
        Description = st.text_area("Description")
        Processor = st.text_input("Processor")
        RAM = st.text_input("RAM")
        Storage = st.text_input("Storage")
        ScreenSize = st.text_input("Screen Size")
        BatteryLife = st.text_input("Battery Life")
        GraphicsCard = st.text_input("Graphics Card")
        OperatingSystem = st.text_input("Operating System")
        submitted = st.form_submit_button("Agregar Producto")
        
        if submitted:
            products_manager.add_product(ProductID, ProductName, Category, Brand, Model, Price, StockQuantity, Description, Processor, RAM, Storage, ScreenSize, BatteryLife, GraphicsCard, OperatingSystem)
            st.success(f"Producto {ProductID} agregado exitosamente")
            st.experimental_rerun()
    
    st.subheader("Modificar Producto")
    with st.form("modify_product_form"):
        ProductID = st.text_input("Product ID a modificar")
        ProductName = st.text_input("Nuevo Product Name")
        Category = st.text_input("Nuevo Category")
        Brand = st.text_input("Nuevo Brand")
        Model = st.text_input("Nuevo Model")
        Price = st.number_input("Nuevo Price", min_value=0.0, format="%.2f")
        StockQuantity = st.number_input("Nuevo Stock Quantity", min_value=0)
        Description = st.text_area("Nueva Description")
        Processor = st.text_input("Nuevo Processor")
        RAM = st.text_input("Nuevo RAM")
        Storage = st.text_input("Nuevo Storage")
        ScreenSize = st.text_input("Nuevo Screen Size")
        BatteryLife = st.text_input("Nueva Battery Life")
        GraphicsCard = st.text_input("Nueva Graphics Card")
        OperatingSystem = st.text_input("Nuevo Operating System")
        submitted = st.form_submit_button("Modificar Producto")
        
        if submitted:
            if products_manager.modify_product(ProductID, ProductName, Category, Brand, Model, Price, StockQuantity, Description, Processor, RAM, Storage, ScreenSize, BatteryLife, GraphicsCard, OperatingSystem):
                st.success(f"Producto {ProductID} modificado exitosamente")
            else:
                st.error(f"Producto {ProductID} no encontrado")
            st.experimental_rerun()
    
    st.subheader("Eliminar Producto")
    with st.form("delete_product_form"):
        ProductID = st.text_input("Product ID a eliminar")
        submitted = st.form_submit_button("Eliminar Producto")
        
        if submitted:
            if products_manager.delete_product(ProductID):
                st.success(f"Producto {ProductID} eliminado exitosamente")
            else:
                st.error(f"Producto {ProductID} no encontrado")
            st.experimental_rerun()

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
