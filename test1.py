import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Olympiad Trainer", layout="centered")
st.title("🏆 OSK Logic Coach")

# Securely get the API Key from a text input
api_key = st.sidebar.text_input("Enter Google API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # Using Gemini 2.0 Flash - The fastest model available right now
    model = genai.GenerativeModel('gemini-2.0-flash')

    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])
        # Initial System Instruction
        st.session_state.chat.send_message(
            "You are a Math Olympiad Coach. Tone: Direct. Method: Socratic (hints only). "
            "Help the student prepare for OSK/OSP/OSN. Never give the answer first."
        )

    # Display chat history
    for message in st.session_state.chat.history:
        role = "assistant" if message.role == "model" else "user"
        with st.chat_message(role):
            st.markdown(message.parts[0].text)

    # User Input
    if prompt := st.chat_input("Ask a math problem or describe your logic..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            # This 'stream=True' makes it feel instant
            response = st.session_state.chat.send_message(prompt, stream=True)
            full_response = st.write_stream(chunk.text for chunk in response)
else:
    st.info("Please enter your API Key from Google AI Studio to start.")
