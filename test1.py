import streamlit as st
from groq import Groq

st.set_page_config(page_title="OSK Coach", layout="centered")
st.title("🏆 OSK Math Logic Coach")

# Use a sidebar for the NEW Groq Key
api_key = st.sidebar.text_input("Enter Groq API Key (gsk_...)", type="password")

if api_key:
    try:
        client = Groq(api_key=api_key)
        
        # This is the 'beast' model for logic
        model_name = "llama-3.3-70b-versatile"
        
        user_input = st.text_input("Explain your logic for an OSK problem:")
        
        if user_input:
            with st.spinner('Coach is calculating...'):
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a Math Olympiad Coach. Use Socratic method. Give hints, not answers."},
                        {"role": "user", "content": user_input}
                    ],
                    model=model_name,
                )
                st.markdown("### 💡 Coach's Hint")
                st.write(chat_completion.choices[0].message.content)
                
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Paste your Groq Key to start. No money required.")
