import google.generativeai as genai
import os
from dotenv import load_dotenv
import requests
load_dotenv()


######################################## For model listing #####################################

# API_KEY = os.getenv("Gemini_API_Key")
# URL = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

# response = requests.get(URL)

# if response.status_code == 200:
#     models = response.json()
#     for model in models.get("models", []):
#         print(f"Model ID: {model['name']}")
#         print(f"  Display Name: {model.get('displayName')}")
#         print(f"  Description: {model.get('description')}")
#         print(f"  Supported Methods: {model.get('supportedGenerationMethods', [])}")
#         print("----")
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)

################################################################################################


# Set up Gemini with your API key
genai.configure(api_key=os.getenv("Gemini_API_Key"))

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")
chat = model.start_chat(history=[])

# Simple chat loop
print("🤖 Gemini Chatbot: Hello! Ask me anything.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    response = chat.send_message(user_input)
    print("Gemini:", response.text)




