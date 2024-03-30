from sqlmodel import SQLModel, Field, create_engine
from typing import Optional
from settings import conn_str

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str

if __name__ == "__main__":    # First time call only   
    engine = create_engine(conn_str)
    SQLModel.metadata.create_all(engine) # Create table on Neon Database where you SQLMODEL inherit and table is true.
