import os
import pandas as pd
from pandasai import Agent

# Establecer la clave de API para pandasai
os.environ["PANDASAI_API_KEY"] = "$2a$10$1iiB1iJAUICKQeUxvW0NouPZy.mKOL0m.Dc.evAz9o1mqqif/v49m"

# Obtener la ruta absoluta del archivo CSV
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "../db/ecommerce_inventory.csv")

def generateResponse(prompt: str):
    db = pd.read_csv(csv_path)
    agent = Agent(db)
    return agent.chat(prompt)

# def generate(self, prompt):
#         context = assistants.get_context_by_id(prompt)

#         model=genai.GenerativeModel(model_name="gemini-1.5-flash",
#                                     system_instruction=context)
        
#         response = model.generate_content(prompt)

#         return response.text