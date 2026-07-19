import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

SYSTEM_INSTRUCTION = """You are a professional, neutral news summarization tool.
Summarize the given article into 3-5 clear bullet points.
Do not include personal opinions, external conclusions, or political bias.
Stay strictly objective and concise."""

try:
    with open("article.txt", "r", encoding="utf-8") as file:
        article = file.read()
except FileNotFoundError:
    print("❌ Error: article.txt not found. Please create the file first.")

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION
        ),
        contents=article
    )
except Exception as e:
    print(f"❌ Error calling the AI model: {e}")

print("\n--- Summary ---")
print(response.text)

with open("summary_output.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

print("\n✅ Summary saved to summary_output.txt")