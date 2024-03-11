from pydantic import BaseModel 
from data import Database
from fastapi import FastAPI 
from fastapi import Body
app=FastAPI()

class Todos(BaseModel):
    title: str

    @app.post("/todos")
    def addTodos(todoTitle:str = Body(embed=True)):
       
       db = Database()
       db.setConnectString("postgresql://hafizshawalnadeem:2DlRFczTPe9J@ep-patient-grass-a52tfj3b.us-east-2.aws.neon.tech/neondb?sslmode=require")
       db.post_method(todoTitle) 
       
       return {"title":todoTitle}

    @app.put("/todos/{todoId}")
    def updateTodos(todoId:int, todoTitle:str = Body(embed=True)):
        db = Database()
        db.setConnectString("postgresql://hafizshawalnadeem:2DlRFczTPe9J@ep-patient-grass-a52tfj3b.us-east-2.aws.neon.tech/neondb?sslmode=require")
        db.put_method(todoId,todoTitle) 

        return {"title":todoTitle}

    @app.delete("/todos/{todoId}")
    def deleteTodos(todoId:int):
        db = Database()
        db.setConnectString("postgresql://hafizshawalnadeem:2DlRFczTPe9J@ep-patient-grass-a52tfj3b.us-east-2.aws.neon.tech/neondb?sslmode=require")
        db.delete_method(todoId)

        return {"title Id":todoId}

    @app.get("/todos")
    def getAllTodos():
        db = Database()
        db.setConnectString("postgresql://hafizshawalnadeem:2DlRFczTPe9J@ep-patient-grass-a52tfj3b.us-east-2.aws.neon.tech/neondb?sslmode=require")
        todos = db.get_all_todos()
        # print("Fast Api")
        # print(todos)
        return todos
