from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated, Any, Dict
from pathlib import Path

class AgentState(TypedDict):
    """
    Represents the structure of the state used in the graph.
    """

    messages : Annotated[list,add_messages]
    frequency : str
    news_data: list[Dict[str, Any]]
    summary: str
    filename: Path



