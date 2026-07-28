from langgraph.graph import StateGraph, START, END

from state import EmailState
from nodes import (
    classify_email,
    important_node, 
    promotion_node,
    spam_node,
    social_node
)

from router import route_email

# Create graph builder

builder = StateGraph(EmailState)

# Add Nodes

builder.add_node("classifier",classify_email)

builder.add_node("important",important_node)

builder.add_node("promotion",promotion_node)

builder.add_node("spam",spam_node)

builder.add_node("social",social_node)


# Connect Start

builder.add_edge(START,"classifier")

builder.add_conditional_edges(
    "classifier",
    route_email,
    {
        "important":"important",
        "promotion":"promotion",
        "spam":'spam',
        "social":"social"
    }
)


# Connect END

builder.add_edge('important',END)

builder.add_edge("promotion",END)

builder.add_edge("spam",END)

builder.add_edge("social",END)

# compile graph

graph = builder.compile()