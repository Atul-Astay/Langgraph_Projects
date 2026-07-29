# graph.py

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from state import FitnessState
from nodes import fitness_coach

# ---------------------------------------
# Create Graph Builder
# ---------------------------------------

builder = StateGraph(FitnessState)

# ---------------------------------------
# Add Nodes
# ---------------------------------------

builder.add_node(
    "fitness_coach",
    fitness_coach
)

# ---------------------------------------
# Define Graph Flow
# ---------------------------------------

builder.add_edge(
    START,
    "fitness_coach"
)

builder.add_edge(
    "fitness_coach",
    END
)

# ---------------------------------------
# Create Memory
# ---------------------------------------

memory = MemorySaver()

# ---------------------------------------
# Compile Graph
# ---------------------------------------

graph = builder.compile(
    checkpointer=memory
)