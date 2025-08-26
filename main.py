import streamlit as st
from agent import create_agent
from langchain.memory import ConversationBufferWindowMemory,ConversationBufferMemory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

# import nest_asyncio
# nest_asyncio.apply()

import asyncio
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


st.set_page_config(page_title="AI Workshop - HR Assistant", page_icon="🤖")

st.title("🤖 AI WORKSHOP - HR Assistant")
msgs = StreamlitChatMessageHistory(key="chat_messages")
memory = ConversationBufferMemory(chat_memory=msgs, return_messages=True, memory_key="chat_history") 
agent = create_agent(memory)

if "messages" not in st.session_state:
    st.session_state["messages"] = []
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
if user_input := st.chat_input("Ask me anything about HR policies, leave, etc..."):
    st.chat_message("user").markdown(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})
    try:
        # print("Memory Before Call", memory.load_memory_variables({}))
        response = agent.invoke({"input": user_input})
        # print("Memory", memory.load_memory_variables({}))
        answer = response.get("output")
    except Exception as e:
        answer = f" Error: {str(e)}"
    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state["messages"].append({"role": "assistant", "content": answer})