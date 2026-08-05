from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph.message import add_messages

from langchain_core.messages import BaseMessage

from graph.profile_schema import UserProfileExtraction


class FitnessState(TypedDict):

    user_id: str

    messages: Annotated[
        list[BaseMessage],
        add_messages,
    ]

    profile: str

    route: str

    profile_data: UserProfileExtraction | None