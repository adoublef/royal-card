from uvicorn import run
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def handle_index():
    return "Hello, World!"    

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=80, proxy_headers=True)
