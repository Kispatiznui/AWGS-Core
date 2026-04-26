from fastapi import FastAPI

app = FastAPI()

@app.post("/simulate")
def simulate(input_text: str):
    return {"status": "running"}
