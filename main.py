from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

html_file = Path(__file__).with_name("index.html")


# Our First API endpoint
@app.get("/")
def read_root():
    return HTMLResponse(content=html_file.read_text(encoding="utf-8"))

@app.get("/chat/{message}")
def chat(message: str):
    return {"message": f"Hello how are you, {message}?"} 