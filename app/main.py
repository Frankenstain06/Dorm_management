from fastapi import FastAPI

app = FastAPI()

@app.get("/{name}")
def w(name: str):
  return {"name" : name}