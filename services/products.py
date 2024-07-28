import pandas as pd
from logger import logger

class ProductInventory:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.load_products()

    def load_products(self):
        self.df = pd.read_csv(self.csv_path)

    def save_products(self):
        self.df.to_csv(self.csv_path, index=False)

    def add_product(self, product_data):
        new_product = pd.Series(product_data)
        self.df = self.df.append(new_product, ignore_index=True)
        self.save_products()

    def modify_product(self, ProductID, product_data):
        lista = self.df["ProductID"].values.tolist()

        if int(ProductID) in lista:
            for key, value in product_data.items():
                self.df.loc[self.df["ProductID"] == int(ProductID), key] = value
            self.save_products()
            return True
        return False

    def delete_product(self, ProductID):
        lista = self.df["ProductID"].values.tolist()
        logger.debug(f"ProductID: {ProductID}, list: {lista}")
        if int(ProductID) in lista:

            self.df = self.df[self.df["ProductID"] != int(ProductID)]
            self.save_products()
            return True
        
        return False

    def get_products(self):
        return self.df
    

