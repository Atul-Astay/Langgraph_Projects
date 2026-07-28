from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from graph import graph

app = FastAPI(
    title="AI Resume Reviewer",
    version="1.0"
)


class ResumeRequest(BaseModel):
    resume: str


class ResumeResponse(BaseModel):
    ats_score: int
    feedback: str
    improved_resume: str
    iterations: int


@app.get("/")
def home():

    return {
        "message": "Resume Reviewer API is Running"
    }


@app.post("/review", response_model=ResumeResponse)
def review_resume(request: ResumeRequest):

    try:

        result = graph.invoke(
            {
                "resume": request.resume,
                "ats_score": 0,
                "feedback": "",
                "improved_resume": "",
                "decision": "",
                "iteration": 0
            }
        )

        return ResumeResponse(
            ats_score=result["ats_score"],
            feedback=result["feedback"],
            improved_resume=result["resume"],
            iterations=result["iteration"]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )