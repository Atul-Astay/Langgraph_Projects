# api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

from graph import graph

app = FastAPI(
    title="AI Fitness Coach API",
    version="1.0.0",
    description="Memory-Based AI Fitness Coach using LangGraph + Gemini"
)


# -----------------------------
# Request Model
# -----------------------------

class ChatRequest(BaseModel):
    thread_id: str
    message: str


# -----------------------------
# Response Model
# -----------------------------

class ChatResponse(BaseModel):
    thread_id: str
    response: str


# -----------------------------
# Home Endpoint
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "🏋️ AI Fitness Coach API is Running!"
    }


# -----------------------------
# Chat Endpoint
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