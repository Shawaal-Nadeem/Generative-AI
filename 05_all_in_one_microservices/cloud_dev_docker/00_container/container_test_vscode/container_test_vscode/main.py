from fastapi import FastAPI

app:FastAPI = FastAPI()

@app.get("/")
def index():
    return {"message": "Container run on VS code"}