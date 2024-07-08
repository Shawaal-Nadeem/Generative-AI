from sqlmodel import Session, select
from class1_poetry.database import *
import todo_pb2


def get_todos(session:Session):
    query = select(Todo)
    todos = session.exec(query).all()
    return todos

async def create_todo(todo: todo_pb2.Todo_proto, session:Session):
    
    todo = Todo(title=todo.title, description=todo.description)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo


def delete_todo(id: int, session:Session):
    todo_delete = session.get(Todo,id)
    session.delete(todo_delete)
    session.commit()
    return {"message": "Todo deleted"}

def update_todo(id: int, todo: todo_pb2.Todo_proto, session:Session):
    todo_update = session.get(Todo, id)
    todo_update.title = todo.title
    todo_update.description = todo.description
    session.commit()
    session.refresh(todo_update)
    return todo_update

