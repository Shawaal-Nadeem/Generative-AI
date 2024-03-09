from fastapi import FastAPI

app=FastAPI()
@app.get("/{who}")
def greet(who:str):
    return {"message":f"Hello {who}"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run("internally_hello:app",reload=True)