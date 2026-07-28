# nodes.py

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from prompts import (
    CLASSIFICATION_PROMPT,
    IMPORTANT_PROMPT,
    PROMOTION_PROMPT,
    SPAM_PROMPT,
    SOCIAL_PROMPT,
)

load_dotenv()

llm = init_chat_model(
    model = 'gemini-2.5-flash',
    model_provider = 'google_genai',    
    temperature = 0
)


# -----------------------------
# Email Classification Node
# -----------------------------
def classify_email(state):
    """
    Classify the email into one of:
    important
    promotion
    spam
    social
    """

    email = state["email"]

    prompt = f"""
{CLASSIFICATION_PROMPT}

Email:

{email}
"""

    response = llm.invoke(prompt)

    category = response.content.strip().lower()

    return {
        "category": category
    }


# -----------------------------
# Important Email Node
# -----------------------------
def important_node(state):

    email = state["email"]

    response = llm.invoke(
        IMPORTANT_PROMPT + "\n" + email
    )

    return {
        "response": response.content
    }


# -----------------------------
# Promotion Email Node
# -----------------------------
def promotion_node(state):

    email = state["email"]

    response = llm.invoke(
        PROMOTION_PROMPT + "\n" + email
    )

    return {
        "response": response.content
    }


# -----------------------------
# Spam Email Node
# -----------------------------
def spam_node(state):

    email = state["email"]

    response = llm.invoke(
        SPAM_PROMPT + "\n" + email
    )

    return {
        "response": response.content
    }


# -----------------------------
# Social Email Node
# -----------------------------
def social_node(state):

    email = state["email"]

    response = llm.invoke(
        SOCIAL_PROMPT + "\n" + email
    )

    return {
        "response": response.content
    }