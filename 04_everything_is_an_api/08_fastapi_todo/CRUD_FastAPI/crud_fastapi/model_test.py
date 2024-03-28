from sqlmodel import SQLModel, Field, create_engine
import os
from dotenv import load_dotenv
from typing import Optional


class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str

if __name__ == "__main__":    # First time call only
    load_dotenv()    
    engine = create_engine(os.getenv("conn_str_test"))
    SQLModel.metadata.create_all(engine) # Create table on Neon Database where you SQLMODEL inherit and table is true.
