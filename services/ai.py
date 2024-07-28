import os
import google.generativeai as genai
import pandas as pd

class AIAssistant:
    def __init__(self, csv_path, api_key):
        self.csv_path = csv_path
        self.api_key = api_key
        genai.configure(api_key=self.api_key)

    def _load_inventory(self):
        try:
            return pd.read_csv(self.csv_path)
        except Exception as e:
            raise Exception(f"Error al cargar el inventario: {e}")

    def generate_response(self, prompt, conversation_history):
        # Cargar los datos del CSV
        df = self._load_inventory()
        context = df.to_string()

        # Instrucción del sistema para el modelo de generación
        system_instruction = (
            "Siempre al principio de la conversación, debes presentarte y dar una breve descripción de tu rol. "
            "Sos un asistente de atención al cliente llamado Marcos que trabaja en MakersTech, usas emojis, eres muy humano, muy amable, carismatico y atento. "
            "Siempre vas al grano y eres muy eficiente. Por favor, responde a las siguientes preguntas "
            "sobre el inventario de la empresa. El máximo de tu respuesta son dos oraciones, debes ser directo y preciso."
        )

        # Verificar si es el primer mensaje de la conversación
        full_prompt = f"{context}\n{conversation_history}\nUsuario: {prompt}\nMarcos:"

        try:
            # Configuración del modelo de generación
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=system_instruction
            )

            # Generar la respuesta
            response = model.generate_content(full_prompt)

            # Agregar la respuesta generada al historial de la conversación
            conversation_history += f"\nUsuario: {prompt}\nMarcos: {response.text}"

            return response.text, conversation_history
        except Exception as e:
            raise Exception(f"Error al generar la respuesta: {e}")
