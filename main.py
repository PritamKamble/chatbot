import os
from dotenv import load_dotenv

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from google import genai

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

app = FastAPI()

html_file = Path(__file__).with_name("index.html")

client = genai.Client()


# Our First API endpoint
@app.get("/")
def read_root():
    return HTMLResponse(content=html_file.read_text(encoding="utf-8"))

@app.get("/chat/{message}")
def chat(message: str):
    print(f"Received message: {message}")
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=message
    )
    print(interaction.output_text)
    return {"response": interaction.output_text}