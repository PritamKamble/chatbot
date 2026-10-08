from fastapi import FastAPI

app = FastAPI()

# Our First API endpoint
@app.get("/")
def read_root():
    return { "Hello": "World" }