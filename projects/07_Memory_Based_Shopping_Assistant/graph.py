from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from state import ShoppingState
from nodes import shopping_assistant

# Create graph builder

builder = StateGraph(ShoppingState)

# Add Nodes
builder.add_node(
    "shopping_assistant",
    shopping_assistant
)

# Define Graph flow
builder.add_edge(
    START,
    "shopping_assistant"
)

builder.add_edge(
    "shopping_assistant",
    END
)

# Create Memory

memory = MemorySaver()

# Compile graph

graph = builder.compile(
    checkpointer=memory
)