import streamlit as st

click:bool=st.button("Increment")

value:int=0

if click:
    value+=1

st.write("Count : ",value)