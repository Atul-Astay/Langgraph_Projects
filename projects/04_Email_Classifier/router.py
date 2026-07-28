# router.py

def route_email(state):
    """
    Route the workflow based on the email category.
    """

    category = state["category"].strip().lower()

    if category == "important":
        return "important"

    elif category == "promotion":
        return "promotion"

    elif category == "spam":
        return "spam"

    else:
        return "social"