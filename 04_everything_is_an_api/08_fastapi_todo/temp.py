from fastapi import FastAPI, Body
import requests

app = FastAPI()
data = {"who": "Shawaal"}

# Send a POST request to the FastAPI endpoint
response = requests.post("http://127.0.0.1:8000/hi", json=data)

@app.post("/hi")
def greet_post(who:str = Body(embed=True)):
    return f"Hello? {who}?"


