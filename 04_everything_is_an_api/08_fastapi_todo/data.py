from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session 
from sqlalchemy import text

class Database():
    _connectString:str
    _engine:Engine

    def __init__(self):
        pass

    def setConnectString(self,conStr:str):
        self._connectString= conStr
        # print("Database Class")
        # print(self._connectString)
        self._engine=create_engine(self._connectString)
        # print(_engine)

    def post_method(self,todo:str):
        # print("Database Class")
        # print(todo)
        # print(self._connectString)
        with Session(self._engine) as session:
            session.execute(text("CREATE TABLE IF NOT EXISTS todos (id SERIAL PRIMARY KEY, todo VARCHAR(255))")) 
            insertionQuery = text(f"INSERT INTO todos (todo) VALUES ('{todo}')")
            jsonFormattedValue = {
                "todo": todo
            }
            session.execute(insertionQuery,jsonFormattedValue)
            session.commit()
        
    def get_all_todos(self):
        with Session(self._engine) as session:
            session.execute(text("CREATE TABLE IF NOT EXISTS todos (id SERIAL PRIMARY KEY, todo VARCHAR(255))"))
            todos = session.execute(text("SELECT * FROM todos"))
            # print("Database Class Get All Todos")
            arr_tuple_todos = list(todos)
            # print(arr_tuple_todos)
            arr_dict_todos = []
            for todo in arr_tuple_todos:
                data_dict = {
                    "id": todo[0],
                    "title": todo[1]
                }
                arr_dict_todos.append(data_dict)
            
            # print(arr_dict_todos)
            return arr_dict_todos

