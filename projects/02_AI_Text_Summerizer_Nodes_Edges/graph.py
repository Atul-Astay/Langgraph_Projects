from langgraph.graph import StateGraph, START, END

from nodes import summarize_node
from state import SummaryState

builder = StateGraph(SummaryState)

builder.add_node("summarize", summarize_node)

builder.add_edge(START, "summarize")
builder.add_edge("summarize", END)

graph = builder.compile()