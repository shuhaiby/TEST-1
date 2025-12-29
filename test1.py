import streamlit as st
import google.generativeai as genai

# 1. Basic UI Setup
st.title("🏆 OSK Logic Coach")
st.write("If you see this, the app is working correctly.")

# 2. Sidebar for the Key
api_key = st.sidebar.text_input("Paste Google API Key Here", type="password")

if api_key:
    try:
        # 3. Setup Gemini
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash') # Using 1.5 for stability
        
        # 4. Simple Input
        user_input = st.text_input("Ask a math question:")
        
        if user_input:
            with st.spinner('Thinking...'):
                response = model.generate_content(user_input)
                st.subheader("Coach's Hint:")
                st.write(response.text)
                
    except Exception as e:
        st.error(f"Something went wrong: {e}")
else:
    st.info("Waiting for API Key... Get it from aistudio.google.com")
