from langchain_core.messages import SystemMessage

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from .state import FitnessState
from .prompts import SYSTEM_PROMPT

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
)


def fitness_coach(state: FitnessState) -> FitnessState:
    """
    Main AI node.
    """

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"],
    ]

    response = llm.invoke(messages)

    return {
        "messages": [response]
    }