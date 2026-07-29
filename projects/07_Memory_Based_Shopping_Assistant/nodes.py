from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage

from config import MODEL_NAME
from prompts import SHOPPING_SYSTEM_PROMPT

load_dotenv()

llm = init_chat_model(
    model = MODEL_NAME,
    model_provider='google_genai'
)

# Shopping assistant node
def shopping_assistant(state):
    """
    Main Shopping assistant node

    state['messages'] already contains the complete
    conversation history.
    """

    # Create system prompt
    system_message = SystemMessage(
        content = SHOPPING_SYSTEM_PROMPT
    )

    # Combine system prompt + Conversation
    messages = [system_message] + state["messages"]

    # Call gemini

    response = llm.invoke(messages)

    return {
        "messages":[response]
    }