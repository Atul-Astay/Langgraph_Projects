from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from config import MAX_ITERATIONS
from prompts import REVIEW_PROMPT, IMPROVE_PROMPT

load_dotenv()

llm  = init_chat_model(
    model = "gemini-2.5-flash",
    model_provider="google_genai"
)

# review essay node

def review_node(state):

    essay = state['essay']

    prompt = REVIEW_PROMPT + "\n\nEssay:\n\n" + essay

    response = llm.invoke(prompt)

    result = response.content.strip()

    decision = "improve"

    if "Decision:finish" in result:
        decision = "finish"

    feedback = ""

    if "Feedback:" in result:
        feedback = result.split("Feedback")[-1].strip()

    return {
        "feedback":feedback,
        "decision":decision
    }

# Improve essay node

def improve_node(state):

    essay = state['essay']
    feedback = state['feedback']

    prompt = IMPROVE_PROMPT.format(
        essay = essay,
        feedback = feedback
    )

    response = llm.invoke(prompt)

    improved = response.content.strip()

    return {
        "essay": improved,
        "improved_essay": improved,
        "iteration": state["iteration"] + 1
    }

# Safety node
# prevent infinite loop

def check_iteration_node(state):

    if state['iteratioin'] >= MAX_ITERATIONS:

        return {
            "decisioin":"finish"
        }
    return {}