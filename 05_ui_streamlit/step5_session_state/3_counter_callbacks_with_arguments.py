import streamlit as st

st.write(st.session_state)

if 'count' not in st.session_state:
    st.session_state.count=0


def increment(val):
    st.session_state.count+=val
    
def decrement(val):
    if st.session_state.count >0:
        st.session_state.count-=val


st.button("Increment",on_click=increment,args=(2,))
st.button("Decrement",on_click=decrement,args=(2,))


st.write("Count : ",st.session_state.count)