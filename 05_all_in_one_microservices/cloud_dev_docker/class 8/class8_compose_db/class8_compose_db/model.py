from sqlmodel import SQLModel, Field, create_engine
from typing import Optional

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str

if __name__ == "__main__":    # First time call only   
    engine = create_engine("postgresql://hafizshawalnadeem:2DlRFczTPe9J@ep-patient-grass-a52tfj3b.us-east-2.aws.neon.tech/cloud_dev_todos_db?sslmode=require")
    SQLModel.metadata.create_all(engine) # Create table on Neon Database where you SQLMODEL inherit and table is true.