import pandas as pd
import os

class ProductInventory:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = self._load_csv()

    def _load_csv(self):
        if os.path.exists(self.csv_path):
            return pd.read_csv(self.csv_path)
        else:
            return pd.DataFrame(columns=[
                'Product ID', 'Product Name', 'Category', 'Brand', 'Model', 'Price',
                'Stock Quantity', 'Description', 'Processor', 'RAM', 'Storage',
                'Screen Size', 'Battery Life', 'Graphics Card', 'Operating System'
            ])

    def _save_csv(self):
        self.df.to_csv(self.csv_path, index=False)

    def get_products(self):
        return self.df.to_dict(orient='records')

    def add_product(self, product):
        self.df = pd.concat([self.df, pd.DataFrame([product])], ignore_index=True)
        self._save_csv()
        return product['Product ID']

    def modify_product(self, product_id, updated_product):
        index = self.df.index[self.df['Product ID'] == product_id].tolist()
        if index:
            index = index[0]
            for key, value in updated_product.items():
                self.df.at[index, key] = value
            self._save_csv()
            return product_id
        else:
            return None

    def delete_product(self, product_id):
        index = self.df.index[self.df['Product ID'] == product_id].tolist()
        if index:
            self.df = self.df.drop(index)
            self._save_csv()
            return product_id
        else:
            return None
