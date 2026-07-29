from fastapi import FastAPI
from pydantic import BaseModel

from graph import graph

app = FastAPI(
    title="Essay Improver API",
    version="1.0"
)

class EssayRequest(BaseModel):
    essay: str

class EssayResponse(BaseModel):
    original_essay : str
    improved_essay : str
    feedback : str
    iterations : str

@app.get("/")
def home():

    return {
        "messege": "Essay Improver API is running"
    }

@app.post("/improve",response_model=EssayResponse)
def improve_essay(request:EssayRequest):

    result = graph.invoke(
        {
            "essay":request.essay,
            "feedback": "",
            "improved_essay":"",
            "decision":"",
            "iteration":0
        }
    )
    return EssayResponse(
        original_essay=request.essay,
        improved_essay=result['essay'],
        feedback = result['feedback'],
        iterations=result['iteration']
    )