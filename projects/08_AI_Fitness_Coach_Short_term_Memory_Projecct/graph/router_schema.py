from typing import Literal

from pydantic import BaseModel, Field


class RouteDecision(BaseModel):
    """
    Route selected by the LLM.
    """

    route: Literal[
        "profile",
        "workout",
        "diet",
        "coach",
    ] = Field(
        description="The next node that should handle the user's request."
    )