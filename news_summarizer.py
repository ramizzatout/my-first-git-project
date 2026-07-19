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


article_files = ["article.txt", "article2.txt", "article3.txt"]

for filename in article_files:

    try:
        with open(filename, "r", encoding="utf-8") as file:
            article = file.read()
    except FileNotFoundError:
        print(f"❌ {filename} not found, skipping...")
        continue


    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION
            ),
            contents=article
        )
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")
        continue

    output_filename = f"summary_{filename}"
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(response.text)

    print(f"✅ {filename} summarized → saved to {output_filename}")