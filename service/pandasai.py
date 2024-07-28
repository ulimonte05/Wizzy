import os
import pandas as pd
from pandasai import Agent

os.environ["PANDASAI_API_KEY"] = "$2a$10$1iiB1iJAUICKQeUxvW0NouPZy.mKOL0m.Dc.evAz9o1mqqif/v49m"

def generateResponse (prompt : str):
    db = pd.read_csv("./../db/ecommerce_inventory.csv")
    
    agent = Agent(db)

    return agent.chat(prompt)

# def generate(self, prompt):
#         context = assistants.get_context_by_id(prompt)

#         model=genai.GenerativeModel(model_name="gemini-1.5-flash",
#                                     system_instruction=context)
        
#         response = model.generate_content(prompt)

#         return response.text