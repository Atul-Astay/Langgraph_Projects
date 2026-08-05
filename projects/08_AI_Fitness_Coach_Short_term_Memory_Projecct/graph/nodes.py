from langchain_core.messages import SystemMessage

from .agents import coach_llm
from .prompts import COACH_PROMPT

from dotenv import load_dotenv

load_dotenv()

def fitness_coach(state):

    messages = [
        SystemMessage(content=COACH_PROMPT),
        *state["messages"],
    ]

    response = coach_llm.invoke(messages)

    return {
        "messages": [response]
    }