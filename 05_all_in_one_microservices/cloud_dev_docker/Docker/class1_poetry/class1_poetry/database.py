from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Generator, Optional
from dotenv import load_dotenv
import os
from contextlib import contextmanager



load_dotenv()

@contextmanager
def get_Session()->Generator[Session,None,None]:
    engine = create_engine(os.getenv("conn_str"))
    with Session(engine) as session:
        yield session


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str


class CreateTodo(SQLModel):
    title: str
    description: str    

if __name__ == "__main__":    # First time call only   
    engine = create_engine(os.getenv("conn_str"))
    SQLModel.metadata.create_all(engine) # Create table on Neon Database where you SQLMODEL inherit and table is true.
