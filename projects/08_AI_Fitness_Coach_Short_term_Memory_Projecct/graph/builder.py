from langgraph.graph import START, END, StateGraph

from .state import FitnessState

from .router import router
from .nodes import fitness_coach
from .workout_node import workout_node
from .diet_node import diet_node
from .profile_node import profile_node
from .save_profile_node import save_profile_node
from .memory import checkpointer

builder = StateGraph(FitnessState)

builder.add_node("router", router)
builder.add_node("coach", fitness_coach)
builder.add_node("workout", workout_node)
builder.add_node("diet", diet_node)
builder.add_node("profile", profile_node)
builder.add_node("save_profile",save_profile_node)

builder.add_edge(START, "router")


def route(state: FitnessState):

    return state["route"]


builder.add_conditional_edges(
    "router",
    route,
    {
        "profile": "profile",
        "workout": "workout",
        "diet": "diet",
        "coach": "coach",
    },
)

builder.add_edge("coach", END)
builder.add_edge("workout", END)
builder.add_edge("diet", END)
builder.add_edge("profile", END)
builder.add_edge("save_profile",END)

graph = builder.compile(
    checkpointer=checkpointer,
)