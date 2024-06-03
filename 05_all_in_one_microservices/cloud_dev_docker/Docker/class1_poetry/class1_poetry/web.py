import streamlit as st
import requests
import pandas as pd


st.header("Todos App")
tab1, tab2, tab3 = st.tabs(["Create", "Update", "Delete"])

with tab1:
    todo = st.text_input("Enter a todo", key='create_todo')
    todo_desc = st.text_input("Enter a todo description", key='create_desc')
    if st.button("Confirm", key='create_button'):
        res = requests.post("http://localhost:8000/todos", json={"title": todo, "description":todo_desc})
        # st.write(res.json())
        st.success(f"{todo} Added")


with tab2:
    todo = st.text_input("Enter a todo for update", key='update_todo')
    todo_desc = st.text_input("Enter a todo description", key='update_desc')
    idVal = st.number_input("Enter ID to update", step=1, format="%d", key='update_id')
    if st.button("Confirm", key='update_confirm'):
        res = requests.put(f"http://localhost:8000/todos/{idVal}", json={"title": todo, "description":todo_desc})
        # st.write(res.json())
        st.success(f"Todo Updated having ID {idVal}")

with tab3:
    idVal = st.number_input("Enter ID to delete", step=1, format="%d", key='delete_id')
    if st.button("Confirm", key='delete_confirm'):
        res = requests.delete(f"http://localhost:8000/todos/{idVal}")
        # st.write(res.json())
        st.success(f"Deleted successfully having ID {idVal}")

st.header("Todos")
response = requests.get("http://localhost:8000/todos")
data = response.json()
df = pd.DataFrame(data)
df_reorder = df[['id', 'title', 'description']]
st.table(df_reorder)