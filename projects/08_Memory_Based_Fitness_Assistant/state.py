# state.py

from langgraph.graph import MessagesState


class FitnessState(MessagesState):
    """
    State used by the Fitness Coach.

    MessagesState automatically stores the
    complete conversation history.

    Example:

    Human -> AI -> Human -> AI

    All messages are stored automatically.
    """

    pass