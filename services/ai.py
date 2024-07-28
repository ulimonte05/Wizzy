import os
import google.generativeai as genai
import pandas as pd

class AIAssistant:
    def __init__(self, csv_path, api_key):
        self.csv_path = csv_path
        self.conversation_history = ""
        self.api_key = api_key
        genai.configure(api_key=self.api_key)

    def _load_inventory(self):
        return pd.read_csv(self.csv_path)

    def generate_response(self, prompt):
        # Cargar los datos del CSV
        df = self._load_inventory()
        context = df.to_string()

        # Instrucción del sistema para el modelo de generación
        system_instruction = (
            "Sos un asistente de atención al cliente llamado Marcos que trabaja en MakersTech, "
            "siempre vas al grano y eres muy eficiente. Por favor, responde a las siguientes preguntas "
            "sobre el inventario de la empresa. El máximo de tu respuesta son dos oraciones, debes ser directo y preciso."
        )

        # Combinar el historial de la conversación con el nuevo prompt y el contexto del inventario
        full_prompt = f"{context}\n{self.conversation_history}\nUsuario: {prompt}\nMarcos:"

        # Configuración del modelo de generación
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction
        )

        # Generar la respuesta
        response = model.generate_content(full_prompt)

        # Agregar la respuesta generada al historial de la conversación
        self.conversation_history += f"\nUsuario: {prompt}\nMarcos: {response.text}"

        return response.text, self.conversation_history

