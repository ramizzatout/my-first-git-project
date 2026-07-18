import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

history = []

print("Chatbot ready. Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    history.append({"role": "user", "parts": [{"text": user_input}]})

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=history
    )

    print(f"AI: {response.text}")

    history.append({"role": "model", "parts": [{"text": response.text}]})