from pydantic import BaseModel 
from data import Database
from fastapi import FastAPI 
from fastapi import Body
import streamlit as st
app=FastAPI()

class Todos(BaseModel):
    title: str

    @app.post("/todos")
    def addTodos(todoTitle:str = Body(embed=True)):
       
       db = Database()
       db.setConnectString(st.secrets["conn_str"])
       db.post_method(todoTitle) 
       
       return {"title":todoTitle}

    @app.put("/todos/{todoId}")
    def updateTodos(todoId:int, todoTitle:str = Body(embed=True)):
        db = Database()
        db.setConnectString(st.secrets["conn_str"])
        db.put_method(todoId,todoTitle) 

        return {"title":todoTitle}

    @app.delete("/todos/{todoId}")
    def deleteTodos(todoId:int):
        db = Database()
        db.setConnectString(st.secrets["conn_str"])
        db.delete_method(todoId)

        return {"title Id":todoId}

    @app.get("/todos")
    def getAllTodos():
        db = Database()
        db.setConnectString(st.secrets["conn_str"])
        todos = db.get_all_todos()
        # print("Fast Api")
        # print(todos)
        return todos