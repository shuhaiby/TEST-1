import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Olympiad Trainer", layout="centered")
st.title("🏆 OSK Logic Coach")

api_key = st.sidebar.text_input("Enter Google API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # We use gemini-2.0-flash because it's the fastest and smartest for math in 2025
        # The 'models/' prefix is crucial to avoid the 404 error
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        
        user_input = st.text_input("Ask your math question or paste your logic:")
        
        if user_input:
            with st.spinner('Coach is thinking...'):
                response = model.generate_content(user_input)
                st.markdown("### 💡 Coach's Hint")
                st.write(response.text)
                
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("Try using 'models/gemini-2.0-flash-lite' if the error persists.")
else:
    st.info("Awaiting API Key... Get yours at aistudio.google.com")
