from fastapi import Depends, FastAPI
from typing import Annotated
from sqlmodel import SQLModel, Field, create_engine, Session, select

app:FastAPI = FastAPI()


class Todo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str

class CreateTodo(SQLModel):
    title: str
    description: str

def get_Session():
    engine = create_engine("postgresql://hafizshawalnadeem:2DlRFczTPe9J@ep-patient-grass-a52tfj3b.us-east-2.aws.neon.tech/cloud_dev_todos_db?sslmode=require")
    with Session(engine) as session:
        yield session

@app.get('/')
def index():
    return {'message':'Hello world!'}

@app.get('/todos')
def getTodo(session:Annotated[dict,Depends(get_Session)]):
    query = select(Todo)
    result = session.exec(query).all()
    return result

@app.post('/todos')
def createTodo(todo:CreateTodo, session:Annotated[dict, Depends(get_Session)]):
    todo = Todo.model_validate(todo)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo