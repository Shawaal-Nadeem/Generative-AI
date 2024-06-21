from fastapi import Depends, FastAPI
from sqlmodel import Field, SQLModel, Session, create_engine, select
from typing import Annotated
from .settings import conn_str  

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import asyncio

import todo_pb2

async def consume(topic:str, bootstrap_servers:str):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        group_id="my-group")
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.value)
            # Deserialize Data
            get_data = todo_pb2.Todo_proto()
            get_data.ParseFromString(msg.value)
            print(f"Deserialize Data : ", {get_data.title , get_data.description})
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


def lifespan(app:FastAPI):
    print("Consumer Start .....")
    asyncio.create_task(consume(topic="todos", bootstrap_servers="broker:19092"))
    yield

# print(conn_str)

class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str

class CreateTodo(SQLModel):
    title: str
    description: str



app = FastAPI(lifespan=lifespan)

def get_Session():
    engine = create_engine(conn_str)
    with Session(engine) as session:
        yield session

@app.get("/todos")
def get_todos(session:Annotated[dict,Depends(get_Session)]):
    query = select(Todo)
    todos = session.exec(query).all()
    return todos

@app.post("/todos")
async def create_todo(todo: CreateTodo, session:Annotated[dict,Depends(get_Session)]):
    producer = AIOKafkaProducer(bootstrap_servers='broker:19092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        todo = Todo.model_validate(todo)
        # session.add(todo)
        # session.commit()
        # session.refresh(todo)
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
