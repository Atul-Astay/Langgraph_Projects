# router.py

from config import MAX_ITERATIONS, TARGET_ATS_SCORE


def review_router(state):
    """
    Decide whether to improve the resume again
    or finish the workflow.
    """

    # Stop if maximum iterations reached
    if state["iteration"] >= MAX_ITERATIONS:
        return "finish"

    # Stop if ATS score is already good
    if state["ats_score"] >= TARGET_ATS_SCORE:
        return "finish"

    # Use reviewer's decision
    decision = str(state["decision"]).lower().strip()

    if decision == "improve":
        return "improve"

    return "finish"