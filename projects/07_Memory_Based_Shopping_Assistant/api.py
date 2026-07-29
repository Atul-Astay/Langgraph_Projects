# api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

from graph import graph

app = FastAPI(
    title="Memory Based Shopping Assistant",
    version="1.0.0",
    description="Shopping Assistant powered by LangGraph + Gemini + Memory"
)


# -----------------------------
# Request Schema
# -----------------------------

class ChatRequest(BaseModel):
    thread_id: str
    message: str


# -----------------------------
# Response Schema
# -----------------------------

class ChatResponse(BaseModel):
    thread_id: str
    response: str


# -----------------------------
# Home Route
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Shopping Assistant API is Running 🚀"
    }


# -----------------------------
# Chat Route
# -----------------------------

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        result = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=request.message)
                ]
            },
            config={
                "configurable": {
                    "thread_id": request.thread_id
                }
            }
        )

        ai_response = result["messages"][-1].content

        return ChatResponse(
            thread_id=request.thread_id,
            response=ai_response
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )