from fastapi import FastAPI, Depends
from typing import Annotated, AsyncGenerator
from sqlmodel import Session
from class1_poetry.services.todo_services import *
import asyncio
from contextlib import asynccontextmanager
import todo_pb2
from class1_poetry.services.consumer import *
from aiokafka import AIOKafkaProducer

@asynccontextmanager
async def lifespan(app:FastAPI)->AsyncGenerator: 
    print("Consumer Lifespan Start ......")
    task = asyncio.create_task(consume_todo(topic="todos", bootstrap_servers="broker:19092"))
    yield
    task.cancel()


app:FastAPI = FastAPI(lifespan=lifespan)

@app.get("/")
def main_page():
    return {"message" : "Todos Page (/todos to the url to see todos)"}

@app.get("/todos")
def get_Todos(session: Annotated[Session, Depends(get_session_dependency)]):
    return get_todos(session=session)

@app.post("/todos")
async def post_Todo(todo:CreateTodo):
    producer = AIOKafkaProducer(bootstrap_servers='broker:19092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        todo = Todo.model_validate(todo)
        add_data = todo_pb2.Todo_proto(
            title=todo.title,
            description=todo.description
        )
        # Serialize Data
        protoc_data = add_data.SerializeToString()
        print(f"Serialize Data : ", {protoc_data})
        await producer.send_and_wait(topic = "todos", value = protoc_data)  
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

    return todo.model_dump_json()       



@app.put("/todos/{id}")
def put_Todo(id: int, todo:CreateTodo, session: Annotated[Session, Depends(get_session_dependency)]):
    return update_todo(id=id, todo=todo, session=session)

@app.delete("/todos/{id}")
def delete_Todo(id: int, session: Annotated[Session, Depends(get_session_dependency)]):
    return (delete_todo(id=id, session=session))