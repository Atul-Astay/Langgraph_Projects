from fastapi import FastAPI
from langchain_core.messages import HumanMessage

from graph.builder import graph
from database.database import Base, engine

app = FastAPI(title="AI Fitness Coach")

Base.metadata.create_all(bind=engine)

@app.get("/")
async def home():
    return {
        "message": "AI Fitness Coach Running 🚀"
    }


@app.get("/chat")
async def chat(
    thread_id: str,
    message: str,
):

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=message)
            ]
        },
        config=config,
    )

    return {
        "thread_id": thread_id,
        "response": result["messages"][-1].content
    }