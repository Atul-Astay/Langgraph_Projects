# router.py

def route_query(state):
    """
    Route the workflow based on the detected intent.
    """

    intent = state["intent"].strip().lower()

    if intent == "billing":
        return "billing"

    elif intent == "technical":
        return "technical"

    else:
        return "general"