from typing_extensions import TypedDict


class CustomerSupportState(TypedDict):
    """
    State that moves through the LangGraph workflow.
    """

    # User's original question
    query: str

    # Intent detected by the router
    intent: str

    # Final response returned to the user
    response: str