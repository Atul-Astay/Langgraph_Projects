# nodes.py

from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage

from config import MODEL_NAME
from prompts import FITNESS_SYSTEM_PROMPT

load_dotenv()

# ----------------------------------------
# Initialize Gemini Model
# ----------------------------------------

llm = init_chat_model(
    model=MODEL_NAME,
    model_provider="google_genai"
)

# ----------------------------------------
# Fitness Coach Node
# ----------------------------------------

def fitness_coach(state):
    """
    Main Fitness Coach Node

    MessagesState automatically provides
    the complete conversation history.
    """

    # Create System Prompt
    system_message = SystemMessage(
        content=FITNESS_SYSTEM_PROMPT
    )

    # Combine system prompt with conversation history
    messages = [system_message] + state["messages"]

    # Call Gemini
    response = llm.invoke(messages)

    # Return AI response
    return {
        "messages": [response]
    }