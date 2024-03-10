from fastapi import FastAPI
from data import get_all_creatures
app= FastAPI()

@app.get("/creatures")
def get_creatures():
    return get_all_creatures()