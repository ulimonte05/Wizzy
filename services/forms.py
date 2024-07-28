import streamlit as st
import pandas as pd
from logger import logger

def show_inventory(products_manager):
    st.header("Inventario")

    # Mostrar el inventario actual
    df = pd.DataFrame(products_manager.get_products())
    st.dataframe(df)
    
    # Formulario para agregar producto
    st.subheader("Agregar Producto")
    with st.form("add_product_form"):
        ProductID = st.text_input("ProductID")
        ProductName = st.text_input("ProductName")
        Category = st.text_input("Category")
        Brand = st.text_input("Brand")
        Model = st.text_input("Model")
        Price = st.number_input("Price", min_value=0.0, format="%.2f")
        StockQuantity = st.number_input("StockQuantity", min_value=0)
        Description = st.text_area("Description")
        Processor = st.text_input("Processor")
        RAM = st.text_input("RAM")
        Storage = st.text_input("Storage")
        ScreenSize = st.text_input("ScreenSize")
        BatteryLife = st.text_input("BatteryLife")
        GraphicsCard = st.text_input("GraphicsCard")
        OperatingSystem = st.text_input("OperatingSystem")
        if st.form_submit_button("Agregar Producto"):
            product_data = {
                "ProductID": ProductID,
                "ProductName": ProductName,
                "Category": Category,
                "Brand": Brand,
                "Model": Model,
                "Price": Price,
                "StockQuantity": StockQuantity,
                "Description": Description,
                "Processor": Processor,
                "RAM": RAM,
                "Storage": Storage,
                "ScreenSize": ScreenSize,
                "BatteryLife": BatteryLife,
                "GraphicsCard": GraphicsCard,
                "OperatingSystem": OperatingSystem
            }
            try:
                products_manager.add_product(product_data)
                st.success(f"Producto {ProductID} agregado exitosamente")
                logger.debug(f"Producto agregado: {product_data}")

                df = pd.DataFrame(products_manager.get_products())
                st.header("Inventario Actualizado")
                st.dataframe(df)
            except Exception as e:
                st.error(f"Error al agregar producto: {str(e)}")
                logger.exception("Error al agregar producto")

    # Formulario para modificar producto
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
        if st.form_submit_button("Modificar Producto"):
            product_data = {
                "ProductName": ProductName,
                "Category": Category,
                "Brand": Brand,
                "Model": Model,
                "Price": Price,
                "StockQuantity": StockQuantity,
                "Description": Description,
                "Processor": Processor,
                "RAM": RAM,
                "Storage": Storage,
                "ScreenSize": ScreenSize,
                "BatteryLife": BatteryLife,
                "GraphicsCard": GraphicsCard,
                "OperatingSystem": OperatingSystem
            }
            try:
                if products_manager.modify_product(ProductID, product_data):
                    st.success(f"Producto {ProductID} modificado exitosamente")
                    logger.debug(f"Producto modificado: {ProductID}, {product_data}")

                    df = pd.DataFrame(products_manager.get_products())
                    st.header("Inventario Actualizado")
                    st.dataframe(df)
                else:
                    st.error(f"Producto {ProductID} no encontrado")
                    logger.warning(f"Producto no encontrado para modificar: {ProductID}")
            except Exception as e:
                st.error(f"Error al modificar producto: {str(e)}")
                logger.exception("Error al modificar producto")

    # Formulario para eliminar producto
    st.subheader("Eliminar Producto")
    with st.form("delete_product_form"):
        ProductID = st.text_input("Product ID a eliminar")
        if st.form_submit_button("Eliminar Producto"):
            try:
                logger.debug(f"Deleting product with ID: {ProductID}")
                if products_manager.delete_product(ProductID):
                    st.success(f"Producto {ProductID} eliminado exitosamente")
                    logger.debug(f"Producto eliminado: {ProductID}")
                    
                    df = pd.DataFrame(products_manager.get_products())
                    st.header("Inventario Actualizado")
                    st.dataframe(df)
                else:
                    st.error(f"Producto {ProductID} no encontrado")
                    logger.warning(f"Producto no encontrado para eliminar: {ProductID}")
            except Exception as e:
                st.error(f"Error al eliminar producto: {str(e)}")
                logger.exception("Error al eliminar producto")
