import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "../db/ecommerce_inventory.csv")

df = pd.read_csv(csv_path)

def getProducts():
    return df.to_dict(orient='records')

def addProduct(ProductID, ProductName, Category, Brand, Model, Price, StockQuantity, Description, Processor, RAM, Storage, ScreenSize, BatteryLife, GraphicsCard, OperatingSystem):
    # Crear un nuevo DataFrame con el producto a agregar
    new_product = pd.DataFrame([{
        'Product ID': ProductID,
        'Product Name': ProductName,
        'Category': Category,
        'Brand': Brand,
        'Model': Model,
        'Price': Price,
        'Stock Quantity': StockQuantity,
        'Description': Description,
        'Processor': Processor,
        'RAM': RAM,
        'Storage': Storage,
        'Screen Size': ScreenSize,
        'Battery Life': BatteryLife,
        'Graphics Card': GraphicsCard,
        'Operating System': OperatingSystem
    }])
    
    # Agregar el nuevo producto al DataFrame existente
    global df
    df = pd.concat([df, new_product], ignore_index=True)
    
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv(csv_path, index=False)
    
    # Retornar el ID del nuevo producto
    return ProductID

def modifyProduct(ProductID, ProductName, Category, Brand, Model, Price, StockQuantity, Description, Processor, RAM, Storage, ScreenSize, BatteryLife, GraphicsCard, OperatingSystem):
    # Encontrar el índice del producto a modificar
    index = df.index[df['Product ID'] == ProductID].tolist()
    
    if index:
        index = index[0]
        # Modificar los valores del producto
        df.at[index, 'Product Name'] = ProductName
        df.at[index, 'Category'] = Category
        df.at[index, 'Brand'] = Brand
        df.at[index, 'Model'] = Model
        df.at[index, 'Price'] = Price
        df.at[index, 'Stock Quantity'] = StockQuantity
        df.at[index, 'Description'] = Description
        df.at[index, 'Processor'] = Processor
        df.at[index, 'RAM'] = RAM
        df.at[index, 'Storage'] = Storage
        df.at[index, 'Screen Size'] = ScreenSize
        df.at[index, 'Battery Life'] = BatteryLife
        df.at[index, 'Graphics Card'] = GraphicsCard
        df.at[index, 'Operating System'] = OperatingSystem
        
        # Guardar el DataFrame actualizado en el archivo CSV
        df.to_csv(csv_path, index=False)
        
        # Retornar el ID del producto modificado
        return ProductID
    else:
        return None

def deleteProduct(ProductID):
    # Encontrar el índice del producto a eliminar
    global df
    index = df.index[df['Product ID'] == ProductID].tolist()
    
    if index:
        index = index[0]
        # Eliminar el producto del DataFrame
        df = df.drop(index)
        
        # Guardar el DataFrame actualizado en el archivo CSV
        df.to_csv(csv_path, index=False)
        
        # Retornar el ID del producto eliminado
        return ProductID
    else:
        return None
