from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"text": "Hello World"}


# To run this file write uvicorn filename(without extension):object name (in my case object name is app) --reload on anaconda terminal
# Above case is check output on browser

# If u check output on terminal then write http pathurl(this url is generate when above case done) on anaconda prompt