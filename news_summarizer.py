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

article = input("Please Paste the news article here ... ")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION
    ),
    contents=article
)

print("\n--- Summary ---")
print(response.text)