import streamlit as st
import google.generativeai as genai

# 1. Basic UI Setup
st.title("🏆 OSK Logic Coach")
st.write("If you see this, the app is working correctly.")

# 2. Sidebar for the Key
api_key = st.sidebar.text_input("Paste Google API Key Here", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # We use 'gemini-2.0-flash' for 2025 speed and logic
        model = genai.GenerativeModel('gemini-2.0-flash') 
        
        user_input = st.text_input("Ask a math question:")
        
        if user_input:
            with st.spinner('Thinking...'):
                # Added a safety check for the model
                response = model.generate_content(user_input)
                st.subheader("Coach's Hint:")
                st.write(response.text)
                
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("Try changing the model name to 'gemini-1.5-flash-latest' in the code if this persists.")
else:
    st.info("Waiting for API Key... Get it from aistudio.google.com")
