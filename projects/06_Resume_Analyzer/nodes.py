from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from config import MODEL_NAME
from prompts import REVIEW_PROMPT, IMPROVE_PROMPT
from schemas import ResumeReview

load_dotenv()

# Initialized gemini model
llm = init_chat_model(
    model = MODEL_NAME,
    model_provider='google_genai'
)

# Create Structured llm
structured_llm = llm.with_structured_output(ResumeReview)


# ---------------------------------------
# Review Resume Node
# ---------------------------------------

def review_resume_node(state):

    resume = state["resume"]

    prompt = REVIEW_PROMPT + "\n\n" + resume

    review = structured_llm.invoke(prompt)

    return {
        "ats_score": review.ats_score,
        "feedback": review.feedback,
        "decision": review.decision
    }


# ---------------------------------------
# Improve Resume Node
# ---------------------------------------

def improve_resume_node(state):

    resume = state["resume"]

    feedback = state["feedback"]

    prompt = IMPROVE_PROMPT.format(
        resume=resume,
        feedback=feedback
    )

    response = llm.invoke(prompt)

    improved_resume = response.content.strip()

    return {
        "resume": improved_resume,
        "improved_resume": improved_resume,
        "iteration": state["iteration"] + 1
    }