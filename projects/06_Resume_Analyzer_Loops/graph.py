from langgraph.graph import StateGraph, START, END

from state import ResumeState

from nodes import (
    review_resume_node,
    improve_resume_node
)

from router import review_router

# Create graph builder

builder = StateGraph(ResumeState)

builder.add_node(
    "review",
    review_resume_node
)

builder.add_node(
    "improve",
    improve_resume_node
)

# START

builder.add_edge(
    START,
    "review"
)

# condition routing

builder.add_conditional_edges(
    "review",
    review_router,
    {
        "improve":"improve",
        "finish":END
    }
)

# Loop back

builder.add_edge(
    "improve",
    "review"
)

# Compile

graph = builder.compile()
