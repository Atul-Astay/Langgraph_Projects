from .state import FitnessState


def router(state: FitnessState):

    question = state["messages"][-1].content.lower()

    if any(word in question for word in [
        "weight",
        "height",
        "age",
        "name",
        "goal",
    ]):

        return {
            "route": "profile"
        }

    if any(word in question for word in [
        "workout",
        "exercise",
        "gym",
        "training",
    ]):

        return {
            "route": "workout"
        }

    if any(word in question for word in [
        "diet",
        "protein",
        "calories",
        "meal",
        "nutrition",
    ]):

        return {
            "route": "diet"
        }

    return {
        "route": "coach"
    }