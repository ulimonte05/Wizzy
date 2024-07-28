import os
import google.generativeai as genai
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "../db/ecommerce_inventory.csv")

def generateResponse(prompt):
        df = pd.read_csv(csv_path)
        context = df.to_string()     

        model=genai.GenerativeModel(model_name="gemini-1.5-flash",
                                    system_instruction=f"Sos un asistente de atencion al cliente llamado Marcos que trabaja en MakersTech, los siguientes son los productos de la tienda acerca de los que dara recomendaciones y brindaras atencion: {context}")
        
        response = model.generate_content(prompt)

        return response.text