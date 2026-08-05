from fastapi import FastAPI
from langchain_core.messages import HumanMessage

from database.database import Base, SessionLocal, engine
from database.crud import get_or_create_user

from graph.builder import graph
from schemas.request import ChatRequest
from services.coach import profile_to_text, save_profile

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/chat")
async def chat(request: ChatRequest):

    db = SessionLocal()

    try:
        save_profile(
            db,
            request.user_id,
            request.message,
        )

        user = get_or_create_user(
            db,
            request.user_id,
        )

        profile = profile_to_text(user)

        config = {
            "configurable": {
                "thread_id": request.thread_id
            }
        }

        result = graph.invoke(
    {
        "user_id": request.user_id,
        "messages": [
            HumanMessage(
                content=request.message
            )
        ],
        "profile": profile,
    },
    config=config,
)

        return {
            "response": result["messages"][-1].content
        }

    finally:
        db.close()