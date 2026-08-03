from typing import Annotated

from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage


class FitnessState(TypedDict):
    """
    Shared state used by every LangGraph node.
    """

    messages: Annotated[list[BaseMessage], add_messages]