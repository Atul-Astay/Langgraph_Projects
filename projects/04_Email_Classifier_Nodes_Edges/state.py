from typing_extensions import TypedDict

class EmailState(TypedDict):
    """
    State share across all Langgraph nodes
    """

    # complete email content (Subject + Body)

    email: str

    # Category predicted by the classifier
    category: str 

    # # Final Response shown to the user
    response: str