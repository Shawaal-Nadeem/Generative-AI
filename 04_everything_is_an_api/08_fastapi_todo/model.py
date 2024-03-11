from pydantic import BaseModel 
from data import Database
from fastapi import FastAPI 
from fastapi import Body
app=FastAPI()

class Todos(BaseModel):
    title: str
    @app.post("/todos")
    def addTodos(self, todoTitle:str = Body(embed=True), conStr:str = Body(embed=True)):
       
    #    db = Database()
    #    db.setConnectString(conStr)
    #    db.post_method(todoTitle) 
       data_dict={
           "title": todoTitle
       }
       return f"{data_dict} Added Successfully"

    def deleteTodos(self, todoId:int):
        pass

    def updateTodos(self, todoId:int, todoTitle:str):
        pass

    def getTodos(self, todoId:int):
        pass

    @app.get("/todos")
    def getAllTodos():
        db = Database()
        db.setConnectString("postgresql://hafizshawalnadeem:2DlRFczTPe9J@ep-patient-grass-a52tfj3b.us-east-2.aws.neon.tech/neondb?sslmode=require")
        todos = db.get_all_todos()
        # print("Fast Api")
        # print(todos)
        return todos
