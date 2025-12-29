import streamlit as st
from src.agentic_ai.UI.streamlit_ui.load_ui import LoadStreamlitUI
from src.agentic_ai.LLM.groq_llm import GroqLLM
from src.agentic_ai.Graph.graph_builder import GraphBuilder
from src.agentic_ai.UI.streamlit_ui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():

    #Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load inout from the UI.")
        return
    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_control_input = user_input)
            llm = obj_llm_config.get_llm_model()

            if not llm:
                st.error("Error : LLM Model could not be initialized.")
                return
            
            # Set up Graph based on use case
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error : No Use case Selected.")
                return
            
            # Graph Builder
            graph_builder = GraphBuilder(llm)

            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Graph Setup Failed - {e}")
                return
            
          
        except Exception as e:
            st.error(f"Graph Setup Failed - {e}")
            return
        





   
