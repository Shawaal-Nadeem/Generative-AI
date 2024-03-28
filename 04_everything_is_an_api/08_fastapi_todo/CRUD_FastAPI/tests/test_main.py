from crud_fastapi.main import Session, get_Session, app
from sqlmodel import create_engine
from dotenv import load_dotenv
import os
from fastapi.testclient import TestClient
def test_get_Session():
    load_dotenv()    
    engine = create_engine(os.getenv("conn_str_test"))
    with Session(engine) as session:
        yield session

app.dependency_overrides[get_Session] = test_get_Session

client = TestClient(app)

def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_todo():
    response = client.post("/todos", json={"title": "Test todo", "description": "Test description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test todo"
    assert response.json()["description"] == "Test description"

def test_delete_todo():
    response = client.delete("/todos/2")
    assert response.status_code == 200

def test_update_todo():
    response = client.put("/todos/3", json={"title": "Updated todo", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated todo"
    assert response.json()["description"] == "Updated description"