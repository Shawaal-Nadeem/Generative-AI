import streamlit as st

if 'count' not in st.session_state:
    st.session_state.count=0

iClick:bool=st.button("Increment")
dClick:bool=st.button("Decrement")

if iClick:
    st.session_state.count+=1
    
if dClick:
    if st.session_state.count >0:
        st.session_state.count-=1


st.write("Count : ",st.session_state.count)