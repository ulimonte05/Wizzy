## Wizzy


video = https://youtu.be/7yOE_WBEwyA
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
```bash
python3 -m venv wizzy-env
```

Using virtualenv
```bash
pip install virtualenv
virtualenv wizzy-env
```

2. Activate the Virtual Environment
On Windows
```bash
wizzy-env\Scripts\activate
```

On macOS and Linux
```bash
source wizzy-env/bin/activate
```

3. Install Dependencies
With the virtual environment activated, install the necessary packages:

```bash
pip install -r requirements.txt
```

3. Configure your .env
Use your Gemini API key to run the Assistant.
```bash
API_KEY="XXX"
```

Database Configuration:
Upload your database to the BD folder. Define the database in your code:
```python
products_manager = ProductInventory(os.path.join(os.path.dirname(file), "db/ecommerce_inventory.csv"))
ai_assistant = AIAssistant(os.path.join(os.path.dirname(file), "db/ecommerce_inventory.csv"), os.getenv('API_KEY'))
```

Bot Customization:
Edit the system_instruction variable in ai.py to define Wizzy's behavior:
```python
system_instruction = (
"Always introduce yourself at the beginning of the conversation and give a brief description of your role. "
"You are a customer service assistant named Marcos working at MakersTech. You use emojis, are very human, friendly, charismatic, and attentive. "
"Always get straight to the point and be very efficient. Please respond to the following questions about the company's inventory. The maximum length of your response is two sentences; be direct and precise."
)
```

Contribution
We welcome contributions from the community! Please contact us via email at demo@wizzi.ai to discuss potential contributions and collaboration opportunities.

## Authors: Eduardo Guzmán and Ulises Montenegro

Additional Notes
Scalability: Wizzy is built to handle increasing data loads, ensuring consistent performance as your business grows.
Security: We prioritize data security and compliance with industry standards.
Integration: Wizzy integrates seamlessly with existing e-commerce platforms, providing a plug-and-play solution.
