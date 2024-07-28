import os
import google.generativeai as genai
import pandas as pd

# Ruta al archivo CSV
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "../db/ecommerce_inventory.csv")

# Variable para almacenar el historial de la conversación
conversation_history = ""

def generateResponse(prompt, conversation_history):
    # Cargar los datos del CSV
    df = pd.read_csv(csv_path)
    context = df.to_string()

    # Instrucción del sistema para el modelo de generación
    system_instruction = (
        "Sos un asistente de atención al cliente llamado Marcos que trabaja en MakersTech, "
        "siempre vas al grano y eres muy eficiente. Por favor, responde a las siguientes preguntas "
        "sobre el inventario de la empresa. El máximo de tu respuesta son dos oraciones, debes ser directo y preciso."
    )

    # Combinar el historial de la conversación con el nuevo prompt y el contexto del inventario
    full_prompt = f"{context}\n{conversation_history}\nUsuario: {prompt}\nMarcos:"

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
