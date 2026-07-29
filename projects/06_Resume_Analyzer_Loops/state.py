from typing_extensions import TypedDict


class ResumeState(TypedDict):
    """
    Shared state across the LangGraph workflow.
    """

    resume: str

    ats_score: int

    feedback: str

    improved_resume: str

    decision: str

    iteration: int