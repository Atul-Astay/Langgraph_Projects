from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

from .agents import profile_llm
from .profile_schema import UserProfileExtraction

structured_llm = profile_llm.with_structured_output(
    UserProfileExtraction
)

SYSTEM_PROMPT = """
Extract fitness profile information.

Only extract information that the user explicitly provides.

Never guess values.

Return null for missing fields.
"""


def profile_node(state):

    message = state["messages"][-1].content

    profile = structured_llm.invoke(
        [
            SystemMessage(
                content=SYSTEM_PROMPT
            ),
            HumanMessage(
                content=message
            ),
        ]
    )

    return {
        "profile_data": profile
    }