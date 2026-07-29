from pydantic import BaseModel, Field

class ResumeReview(BaseModel):
    """
    Structured output returned by the resume reviewer
    """

    ats_score: int = Field(
        description="ATS score between 0 to 100"
    )

    decision:str = Field(
        description="Either improve or finish"
    )

    feedback: str = Field(
        description="Detailed feedback for improving the resume"
    )