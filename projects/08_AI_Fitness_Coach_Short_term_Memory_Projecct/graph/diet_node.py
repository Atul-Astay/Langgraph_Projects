from langchain_core.messages import SystemMessage

from .agents import diet_llm
from .prompts import DIET_PROMPT


def diet_node(state):

    messages = [
        SystemMessage(content=DIET_PROMPT),
        *state["messages"],
    ]

    response = diet_llm.invoke(messages)

    return {
        "messages": [response]
    }