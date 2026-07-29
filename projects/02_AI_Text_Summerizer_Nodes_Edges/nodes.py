import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from prompts import SYSTEM_PROMPT

load_dotenv()

llm = init_chat_model(
    model='gemini-2.5-flash',
)

def summarize_node(state):
    article = state["article"]

    prompt = f"""
{SYSTEM_PROMPT}

Article:

{article}
"""

    response = llm.invoke(prompt)

    return {
        "summary": response.content
    }