from langgraph.graph import MessagesState


class ShoppingState(MessagesState):
    """
    State for Shopping Assistant.

    MessagesState already stores:

    messages = [
        HumanMessage(...),
        AIMessage(...),
        ...
    ]

    LangGraph automatically updates this list.
    """

    pass