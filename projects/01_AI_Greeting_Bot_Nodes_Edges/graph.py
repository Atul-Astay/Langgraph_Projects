from langgraph.graph import StateGraph, START, END

from state import GreetingState
from nodes import greeting_node


builder = StateGraph(GreetingState)

builder.add_node("greeting",greeting_node)

builder.add_edge(START,"greeting")
builder.add_edge("greeting",END)

graph = builder.compile()