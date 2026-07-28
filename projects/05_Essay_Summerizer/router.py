# router.py

from config import MAX_ITERATIONS


def review_router(state):
    """
    Decide whether to improve the essay again or finish.
    """

    # Safety check
    if state["iteration"] >= MAX_ITERATIONS:
        return "finish"

    # Decision from Review Node
    decision = state["decision"].lower().strip()

    if decision == "improve":
        return "improve"

    return "finish"