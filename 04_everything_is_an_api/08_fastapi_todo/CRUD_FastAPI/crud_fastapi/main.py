from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from sqlmodel import Field, SQLModel, Session, create_engine
from typing import Annotated
import os


class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str

class CreateTodo(SQLModel):
    title: str
    description: str


app = FastAPI()

def get_Session():
    load_dotenv()
    engine = create_engine(os.getenv("conn_str"))
    with Session(engine) as session:
        yield session

@app.get("/todos")
def get_todos(session:Annotated[dict,Depends(get_Session)]):
    todos = session.query(Todo).all()
    return todos

@app.post("/todos")
def create_todo(todo: CreateTodo, session:Annotated[dict,Depends(get_Session)]):
    todo = Todo.model_validate(todo)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@app.delete("/todos/{id}")
def delete_todo(id: int, session:Annotated[dict,Depends(get_Session)]):
    todo_delete = session.get(Todo,id)
    session.delete(todo_delete)
    session.commit()
    return {"message": "Todo deleted"}

@app.put("/todos/{id}")
def update_todo(id: int, todo: CreateTodo, session:Annotated[dict,Depends(get_Session)]):
    todo_update = session.get(Todo, id)
    todo_update.title = todo.title
    todo_update.description = todo.description
    session.commit()
    session.refresh(todo_update)
    return todo_update