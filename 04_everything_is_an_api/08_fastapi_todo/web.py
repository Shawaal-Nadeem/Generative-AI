import streamlit as st
from model import Todos
import requests
import pandas as pd

st.header("Todos App")

todo:str=st.text_input("Enter a todo")
if todo:
    if st.button("Add"):
        st.success(f"{todo} Added")
        # print(f"{todo} Added ")
        obj=Todos(title=todo)
        connection_string: str = st.secrets['conn_str']
        obj.addTodos(todo,connection_string)

st.header("Todos")
response = requests.get("http://127.0.0.1:8000/todos")
data = response.json()
df = pd.DataFrame(data)
st.write(df)