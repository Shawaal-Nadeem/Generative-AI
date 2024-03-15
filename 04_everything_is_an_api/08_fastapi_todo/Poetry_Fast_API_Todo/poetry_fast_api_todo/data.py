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
        self._engine=create_engine(self._connectString)
       

    def post_method(self,todo:str):

        with Session(self._engine) as session:
            session.execute(text("CREATE TABLE IF NOT EXISTS todos (id SERIAL PRIMARY KEY, todo VARCHAR(255))")) 
            insertionQuery = text(f"INSERT INTO todos (todo) VALUES ('{todo}')")
            jsonFormattedValue = {
                "todo": todo
            }
            session.execute(insertionQuery,jsonFormattedValue)
            session.commit()
        

    def put_method(self, id:int, todo:str):
        with Session(self._engine) as session:
            session.execute(text("CREATE TABLE IF NOT EXISTS todos (id SERIAL PRIMARY KEY, todo VARCHAR(255))"))
            updateQuery = text(f"UPDATE todos SET todo='{todo}' WHERE id={id}")
            jsonFormattedValue = {
                "todo": todo
            }
            session.execute(updateQuery, jsonFormattedValue)
            session.commit()


    def delete_method(self, id:int):
        with Session(self._engine) as session:
            session.execute(text("CREATE TABLE IF NOT EXISTS todos (id SERIAL PRIMARY KEY, todo VARCHAR(255))"))
            deleteQuery = text(f"DELETE FROM todos WHERE id={id}")
            session.execute(deleteQuery)
            session.commit()

    def get_all_todos(self):
        with Session(self._engine) as session:
            session.execute(text("CREATE TABLE IF NOT EXISTS todos (id SERIAL PRIMARY KEY, todo VARCHAR(255))"))
            todos = session.execute(text("SELECT * FROM todos"))
            arr_tuple_todos = list(todos)
            arr_dict_todos = []
            for todo in arr_tuple_todos:
                data_dict = {
                    "id": todo[0],
                    "title": todo[1]
                }
                arr_dict_todos.append(data_dict)
            
            return arr_dict_todos

