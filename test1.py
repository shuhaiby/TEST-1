import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Olympiad Coach", layout="centered")
st.title("🏆 OSK Logic Coach")

# Sidebar for the API Key
api_key = st.sidebar.text_input("Enter Google API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # This code asks Google: "What models am I allowed to use?"
        # It fixes the '404' and 'None of the models responding' error
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # We pick the best one available (Gemini 2.0 or 3 if available)
        best_model = "models/gemini-2.0-flash" if "models/gemini-2.0-flash" in models else models[0]
        
        model = genai.GenerativeModel(best_model)
        
        user_input = st.text_input(f"Ask a math question (Using: {best_model})")
        
        if user_input:
            with st.spinner('Thinking...'):
                response = model.generate_content(user_input)
                st.subheader("Coach's Hint:")
                st.write(response.text)
                
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Paste your key in the sidebar. Get it at aistudio.google.com")
