import streamlit as st

st.write(st.session_state)

if 'count' not in st.session_state:
    st.session_state.count=0


def increment():
    st.session_state.count+=1
    
def decrement():
    if st.session_state.count >0:
        st.session_state.count-=1


st.button("Increment",on_click=increment)
st.button("Decrement",on_click=decrement)


st.write("Count : ",st.session_state.count)