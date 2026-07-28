# graph.py

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from state import EssayState

from nodes import (
    review_node,
    improve_node,
)

from router import review_router


# ---------------------------------
# Create Graph Builder
# ---------------------------------

builder = StateGraph(EssayState)

# ---------------------------------
# Add Nodes
# ---------------------------------

builder.add_node(
    "review",
    review_node,
)

builder.add_node(
    "improve",
    improve_node,
)

# ---------------------------------
# Start Edge
# ---------------------------------

builder.add_edge(
    START,
    "review",
)

# ---------------------------------
# Conditional Routing
# ---------------------------------

builder.add_conditional_edges(
    "review",
    review_router,
    {
        "improve": "improve",
        "finish": END,
    },
)

# ---------------------------------
# Loop Edge
# ---------------------------------

builder.add_edge(
    "improve",
    "review",
)

# ---------------------------------
# Compile Graph
# ---------------------------------

graph = builder.compile()