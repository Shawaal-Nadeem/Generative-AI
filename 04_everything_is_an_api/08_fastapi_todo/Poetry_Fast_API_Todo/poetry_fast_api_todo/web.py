import streamlit as st
import requests
import pandas as pd

st.header("Todos App")

tab1, tab2, tab3 = st.tabs(["Create", "Update", "Delete"])

with tab1:
    todo = st.text_input("Enter a todo", key='create_todo')
    if st.button("Confirm", key='create_button'):
        res = requests.post("http://127.0.0.1:8000/todos", json={"todoTitle": todo})
        # st.write(res.json())
        st.success(f"{todo} Added")


with tab2:
    todo = st.text_input("Enter a todo for update", key='update_todo')
    idVal = st.number_input("Enter ID to update", step=1, format="%d", key='update_id')
    if st.button("Confirm", key='update_confirm'):
        res = requests.put(f"http://127.0.0.1:8000/todos/{idVal}", json={"todoTitle": todo})
        # st.write(res.json())
        st.success(f"Todo Updated having ID {idVal}")

with tab3:
    idVal = st.number_input("Enter ID to delete", step=1, format="%d", key='delete_id')
    if st.button("Confirm", key='delete_confirm'):
        res = requests.delete(f"http://127.0.0.1:8000/todos/{idVal}")
        # st.write(res.json())
        st.success(f"Deleted successfully having ID {idVal}")

st.header("Todos")
response = requests.get("http://127.0.0.1:8000/todos")
data = response.json()
df = pd.DataFrame(data)
st.table(df)