from langgraph.graph import StateGraph, START,END

from state import CustomerSupportState
from nodes import (
    detect_intent,
    billing_node,
    technical_node,
    general_node
)
from router import route_query

builder = StateGraph(CustomerSupportState)

# add nodes
builder.add_node("detect_intent",detect_intent)
builder.add_node("billing",billing_node)
builder.add_node("technical",technical_node)
builder.add_node("general",general_node)

# Start the graph

builder.add_edge(START, "detect_intent")

# Conditional routing
builder.add_conditional_edges(
    "detect_intent",
    route_query,
    {
        'billing':"billing",
        "technical":"technical",
        "general":"general",
    },
)

# End the graph
builder.add_edge("billing",END)
builder.add_edge("technical",END)
builder.add_edge("general",END)

# compile the graph

graph = builder.compile()