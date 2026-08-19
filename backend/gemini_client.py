import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key=os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise RuntimeError("GOOGLE_API_KEY is not set in the environment variables.")

client=genai.Client(api_key=api_key)

response=client.models.generate_content(
    model='gemini-3.6-flash',
    contents="Who is ultimate star in tamilnadu?"
)

print(response.text)


    

