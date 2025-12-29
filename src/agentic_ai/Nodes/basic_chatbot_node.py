from src.agentic_ai.State.state import AgentState

class BasicChatbotNode:
    """
    Basic Chatbot Logic Implementation.
    """

    def __init__(self,model) -> None:
        self.llm = model
    
    def process(self,state : AgentState):
        """
        Process the Input Structure and generate response.   
        """

        return{"messages" : [self.llm.invoke(state["messages"])]}





