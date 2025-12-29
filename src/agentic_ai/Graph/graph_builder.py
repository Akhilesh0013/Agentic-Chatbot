from langgraph.graph import StateGraph
from src.agentic_ai.State.state import AgentState
from langgraph.graph import START , END
from src.agentic_ai.Nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:
    def __init__(self,model) -> None:
        self.llm = model
        self.graph_builder = StateGraph(AgentState)
    
    def basic_chatbot(self):
        """
        Builds a basic chatbot using LangGraph.
        This methos initializes a chatbot node using the BasicChatbotNodeclass
        and integrates it into the graph. The chatbot node is set s both the entry
        and exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process) 
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
    
    def setup_graph(self, usecase):

        if usecase == 'Basic Chatbot':
            self.basic_chatbot()
            
        return self.graph_builder.compile()






    