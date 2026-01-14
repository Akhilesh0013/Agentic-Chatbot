import streamlit as st
import os

from src.agentic_ai.UI.config_ui import Config

class LoadStreamlitUI:
    def __init__(self) -> None:
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), layout= "wide")
        st.header("🤖 " + self.config.get_page_title())

        st.session_state.IsFetchButtonClicked = False
        st.session_state.timeframe = None

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM Selections
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"]= st.session_state["GROQ_API_KEY"] =st.text_input("API Key", type="password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning(" ⚠️ Please Enter Your GROQ API KEY to Proceed.")
            
            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls["selected_usecase"] == 'Chatbot With Web' or self.user_controls["selected_usecase"] == 'AI News Summarizer':
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"] = st.session_state['TAVILY_API_KEY'] = st.text_input("TAVILY API KEY", type="password")

                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home")
                
            if self.user_controls["selected_usecase"] == 'AI News Summarizer' :
                st.subheader("📰 AI News Explorer") 

                with st.sidebar:
                    time_frame = st.selectbox(
                        "📅 Select Time Frame",
                        ["day", "week", "month", "year"],
                        index= 0
                    )
                
                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame

            
        return self.user_controls
    
        
    



