from langgraph.graph import StateGraph
from src.agentic_ai.State.state import AgentState
from langgraph.graph import START , END
from src.agentic_ai.Nodes.basic_chatbot_node import BasicChatbotNode
from src.agentic_ai.Tools.search_tool import get_tools , create_tool_node
from langgraph.prebuilt import tools_condition , ToolNode
from src.agentic_ai.Nodes.chatbot_with_web import ToolChatbotNode


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
    
    def chatbot_with_tools(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node
        and a tool node. It defines and initilizes a chatbot with tool capabilities.
        """

        # Definition of tool and tool node
        tools = get_tools()
        tool_node = create_tool_node(tools)

        # Define Chatbot node
        obj_chatbot_with_node = ToolChatbotNode(self.llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        # Define conditional and direct edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")

    
    def setup_graph(self, usecase):

        if usecase == 'Basic Chatbot':
            self.basic_chatbot()
        
        if usecase == 'Chatbot With Web' :
            self.chatbot_with_tools()
            
        return self.graph_builder.compile()






    