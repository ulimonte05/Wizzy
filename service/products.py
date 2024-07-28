import pandas as pd

df = pd.read_csv("./../db/ecommerce_inventory.csv")

def getProducts():
    return df.to_dict(orient='records')

def addProduct(ProductID, ProductName, Category, Brand, Model, Price, StockQuantity, Description):
    # Crear un nuevo DataFrame con el producto a agregar
    new_product = pd.DataFrame([{
        'Product ID': ProductID,
        'Product Name': ProductName,
        'Category': Category,
        'Brand': Brand,
        'Model': Model,
        'Price': Price,
        'Stock Quantity': StockQuantity,
        'Description': Description
    }])
    
    # Agregar el nuevo producto al DataFrame existente
    global df
    df = pd.concat([df, new_product], ignore_index=True)
    
    # Guardar el DataFrame actualizado en el archivo CSV
    df.to_csv("./../db/ecommerce_inventory.csv", index=False)
    
    # Retornar el ID del nuevo producto
    return ProductID

def modifyProduct(ProductID, ProductName, Category, Brand, Model, Price, StockQuantity, Description):
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
        
        # Guardar el DataFrame actualizado en el archivo CSV
        df.to_csv("./../db/ecommerce_inventory.csv", index=False)
        
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
        df.to_csv("./../db/ecommerce_inventory.csv", index=False)
        
        # Retornar el ID del producto eliminado
        return ProductID
    else:
        return None


