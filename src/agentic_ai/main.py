import streamlit as st
from src.agentic_ai.UI.streamlit_ui.load_ui import LoadStreamlitUI


def load_langgraph_agenticai_app():

    #Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load inout from the UI.")
        return
    
    user_message = st.chat_input("Enter your message:")

   
