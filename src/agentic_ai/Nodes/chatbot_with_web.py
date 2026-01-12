from src.agentic_ai.State.state import AgentState

class ToolChatbotNode:
    """
    Chatbot with web implementation.
    """

    def __init__(self,model) -> None:
        self.llm = model

    def process(self,state:AgentState):

        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke({"role": "user" , "content" : user_input})

        # Simulate tool specific logic
        tools_response = f"Tool integration for : {user_input}"

        return {"messages" : [llm_response, tools_response]}
    
    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """

        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state : AgentState):

            return {"messages" : [llm_with_tools.invoke(state["messages"])]}
        
        
        return chatbot_node

    









    







        