import os
import pandas as pd
from pandasai import Agent

# Conectar CSV
sales_by_country = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "sales": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

os.environ["PANDASAI_API_KEY"] = "YOUR_API_KEY"

agent = Agent(sales_by_country)

def generateResponse (prompt : str):
    return agent.chat(prompt)