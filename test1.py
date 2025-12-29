import streamlit as st
import google.generativeai as genai

st.title("🏆 OSK Logic Coach")

api_key = st.sidebar.text_input("Enter Google API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # This part asks Google: "What models can I actually use?"
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        if not available_models:
            st.error("No models found. Your API key might be restricted.")
        else:
            # We prioritize the newest models if they are in your list
            # gemini-3-flash and gemini-2.5-flash are the standards now
            target_models = ['models/gemini-3-flash', 'models/gemini-2.5-flash', 'models/gemini-2.0-flash']
            
            # Find the best one available in YOUR specific list
            final_model_name = next((m for m in target_models if m in available_models), available_models[0])
            
            user_input = st.text_input(f"Ask a question (Using: {final_model_name})")
            
            if user_input:
                with st.spinner('Coach is thinking...'):
                    model = genai.GenerativeModel(final_model_name)
                    response = model.generate_content(user_input)
                    st.markdown("### 💡 Coach's Hint")
                    st.write(response.text)
                    
    except Exception as e:
        st.error(f"Logic Error: {e}")
else:
    st.info("Paste your API key in the sidebar.")
