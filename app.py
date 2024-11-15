import streamlit as st
from ollama_setup import multimodal_response
import ollama

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by Llama-vision: Multimodal")

# Initialize the session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display existing messages in chat format
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# File uploader for images
uploaded_files = st.file_uploader("Choose an image", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

# Chat input box
if prompt := st.chat_input():
    # Append user message to session state
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    image_paths = [file for file in uploaded_files] if uploaded_files else None
    
    # Generate a response using the multimodal function
    response = multimodal_response(st.session_state["messages"], image=image_paths)
    
    # Append assistant response to session state and display it
    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
