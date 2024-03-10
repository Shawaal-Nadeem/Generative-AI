# Alternate method to see data

from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/hi") 
def greet():
    return "Hello? World? Hi page"

@app.get("/hi/{name}")
def greet_with_name(name: str):
    return "Hello? World, " + name


if __name__ == "__main__":     # it means this is work only 1st time after updatation in file wo not need again n again server to start bcz server is already running
    import uvicorn
    uvicorn.run("hello1:app", reload=True)