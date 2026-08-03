from langgraph.graph import START, END, StateGraph

from .state import FitnessState
from .nodes import fitness_coach
from .memory import checkpointer

builder = StateGraph(FitnessState)

builder.add_node("fitness_coach", fitness_coach)

builder.add_edge(START, "fitness_coach")
builder.add_edge("fitness_coach", END)

graph = builder.compile(
    checkpointer=checkpointer
)