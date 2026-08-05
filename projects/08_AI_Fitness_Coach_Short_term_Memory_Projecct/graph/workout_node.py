from langchain_core.messages import SystemMessage

from .agents import workout_llm
from .prompts import WORKOUT_PROMPT


def workout_node(state):

    messages = [
        SystemMessage(content=WORKOUT_PROMPT),
        *state["messages"],
    ]

    response = workout_llm.invoke(messages)

    return {
        "messages": [response]
    }