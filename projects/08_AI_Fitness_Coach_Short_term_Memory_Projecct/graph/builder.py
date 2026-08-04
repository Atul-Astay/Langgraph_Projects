from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from .nodes import fitness_coach, tools
from .state import FitnessState
from .memory import checkpointer

builder = StateGraph(FitnessState)

builder.add_node("coach", fitness_coach)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "coach")

builder.add_conditional_edges(
    "coach",
    tools_condition,
)

builder.add_edge("tools", "coach")

graph = builder.compile(
    checkpointer=checkpointer,
)