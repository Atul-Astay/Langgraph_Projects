from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq

from .prompts import SYSTEM_PROMPT
from .state import FitnessState
from .tools import (
    beginner_workout,
    calculate_bmi,
    calculate_calories,
    protein_requirement,
    water_requirement,
)

from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
)

tools = [
    calculate_bmi,
    calculate_calories,
    protein_requirement,
    water_requirement,
    beginner_workout,
]

llm_with_tools = llm.bind_tools(tools)


def fitness_coach(state: FitnessState):

    profile = state.get("profile", "")

    messages = [
        SystemMessage(
            content=SYSTEM_PROMPT
            + "\n\nUser Profile:\n"
            + profile
        ),
        *state["messages"],
    ]

    response = llm_with_tools.invoke(messages)

    return {
        "messages": [response]
    }