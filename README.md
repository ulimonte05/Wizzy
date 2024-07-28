Wizzy

Wizzy is an intelligent, Conversational AI-powered chatbot designed to revolutionize the e-commerce experience. By providing real-time product recommendations, inventory updates, and seamless customer interactions, Wizzy ensures an engaging and efficient shopping journey. Embrace the future of retail with Wizzy, your virtual assistant for a smarter, more personalized shopping experience.

Key Features

Real-Time Inventory Updates: Instantly check product availability and manage inventory.
Personalized Product Recommendations: AI-driven insights tailor product suggestions to individual customer preferences.
Cross-Selling and Upselling: Increase sales with strategic product suggestions.
Installation

Follow these steps to set up Wizzy:

1. Environment Setup
Create a virtual environment to manage dependencies efficiently.

Using venv (Python 3.3+)

bash
Copy code
python3 -m venv wizzy-env
Using virtualenv

bash
Copy code
pip install virtualenv
virtualenv wizzy-env
2. Activate the Virtual Environment
On Windows

bash
Copy code
wizzy-env\Scripts\activate
On macOS and Linux

bash
Copy code
source wizzy-env/bin/activate
3. Install Dependencies
With the virtual environment activated, install the necessary packages:

bash
Copy code
pip install -r requirements.txt
Usage

API Key Setup:
Set your Gemini API key in the environment variables or configuration file.
Database Configuration:
Upload your database to the BD folder.
Define the database in your code:
python
Copy code
products_manager = ProductInventory(os.path.join(os.path.dirname(__file__), "db/ecommerce_inventory.csv"))
ai_assistant = AIAssistant(os.path.join(os.path.dirname(__file__), "db/ecommerce_inventory.csv"), os.getenv('API_KEY'))
Bot Customization:
Edit the system_instruction variable in ai.py to define Wizzy's behavior:
python
Copy code
system_instruction = (
    "Siempre al principio de la conversación, debes presentarte y dar una breve descripción de tu rol. "
    "Sos un asistente de atención al cliente llamado Marcos que trabaja en MakersTech, usas emojis, eres muy humano, muy amable, carismático y atento. "
    "Siempre vas al grano y eres muy eficiente. Por favor, responde a las siguientes preguntas "
    "sobre el inventario de la empresa. El máximo de tu respuesta son dos oraciones, debes ser directo y preciso."
)
Contribution

We welcome contributions from the community! Please contact us via email at demo@wizzi.ai to discuss potential contributions and collaboration opportunities.

Authors

Ulises Montenegro
Eduardo Guzmán
Additional Notes

Scalability: Wizzy is built to handle increasing data loads, ensuring consistent performance as your business grows.
Security: We prioritize data security and compliance with industry standards.
Integration: Wizzy integrates seamlessly with existing e-commerce platforms, providing a plug-and-play solution
