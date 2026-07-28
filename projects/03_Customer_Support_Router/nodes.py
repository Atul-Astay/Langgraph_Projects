# nodes.py

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from prompts import (
    INTENT_PROMPT,
    BILLING_PROMPT,
    TECHNICAL_PROMPT,
    GENERAL_PROMPT,
)

load_dotenv()

llm = init_chat_model(
    model = 'gemini-2.5-flash',
    model_provider = 'google_genai',    
    temperature = 0
)


# ----------------------------
# Intent Detection Node
# ----------------------------
def detect_intent(state):
    """
    Detect the category of the user's query.
    """

    query = state["query"]

    prompt = f"""
{INTENT_PROMPT}

User Query:
{query}
"""

    response = llm.invoke(prompt)

    intent = response.content.strip().lower()

    return {
        "intent": intent
    }


# ----------------------------
# Billing Support Node
# ----------------------------
def billing_node(state):
    query = state["query"]

    prompt = BILLING_PROMPT + "\n" + query

    response = llm.invoke(prompt)

    return {
        "response": response.content
    }


# ----------------------------
# Technical Support Node
# ----------------------------
def technical_node(state):
    query = state["query"]

    prompt = TECHNICAL_PROMPT + "\n" + query

    response = llm.invoke(prompt)

    return {
        "response": response.content
    }


# ----------------------------
# General Support Node
# ----------------------------
def general_node(state):
    query = state["query"]

    prompt = GENERAL_PROMPT + "\n" + query

    response = llm.invoke(prompt)

    return {
        "response": response.content
    }