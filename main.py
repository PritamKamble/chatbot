from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_file = Path(__file__).with_name("index.html")


# Our First API endpoint
@app.get("/")
def read_root():
    return HTMLResponse(content=html_file.read_text(encoding="utf-8"))

# API Addition of 2 numbers
@app.get("/add/{num1}/{num2}")
def add_numbers(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}