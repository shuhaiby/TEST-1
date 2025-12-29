import streamlit as st
import google.generativeai as genai

st.title("🏆 OSK Logic Coach")

api_key = st.sidebar.text_input("Enter Google API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # We try a list of models from newest to most stable
        model_names = ['gemini-2.0-flash', 'gemini-1.5-flash-latest', 'gemini-1.5-flash']
        
        user_input = st.text_input("Ask your math question:")
        
        if user_input:
            with st.spinner('Coach is thinking...'):
                # Automatic fallback logic
                success = False
                for name in model_names:
                    try:
                        model = genai.GenerativeModel(name)
                        response = model.generate_content(user_input)
                        st.markdown(f"### 💡 Coach's Hint (Model: {name})")
                        st.write(response.text)
                        success = True
                        break # Stop if it works
                    except:
                        continue # Try next model if 404
                
                if not success:
                    st.error("None of the models are responding. Check if your API Key is active at aistudio.google.com")
                
    except Exception as e:
        st.error(f"General Error: {e}")
else:
    st.info("Awaiting API Key... Get yours at aistudio.google.com")
