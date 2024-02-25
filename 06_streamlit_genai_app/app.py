import streamlit as st
from model import BotModel


st.title("Streamlit Chatbot")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

if "bot" not in st.session_state:
    st.session_state['bot']=BotModel("My ChatBot")

with st.sidebar:
    if st.button('Delete Chat History'):
        st.session_state['bot'].deleteChatHistory()

for i in st.session_state['bot'].getMessage():
    if i["role"] == "user":
        avatar = USER_AVATAR
    else:
        avatar = BOT_AVATAR

    with st.chat_message(i['role']):
        st.markdown(i['content'])

# Main chat interface
if prompt := st.chat_input("How can I help?"):

    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        message_placeholder = st.empty()
        full_response = ""
        for response in st.session_state.bot.sendMessage({"role": "user", "content": prompt}):
            full_response += response.choices[0].delta.content or ""
            message_placeholder.markdown(full_response + "|")
        message_placeholder.markdown(full_response)
    
    st.session_state.bot.appendMessage({"role": "assistant", "content": full_response})

# Save chat history after each interaction
st.session_state.bot.saveChatHistory()