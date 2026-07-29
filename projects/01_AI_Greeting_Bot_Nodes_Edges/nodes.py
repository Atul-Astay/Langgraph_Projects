import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool

load_dotenv()

llm = init_chat_model(
    model = 'gemini-2.5-flash',
    model_provider = 'google_genai',    
    temperature = 0
)

def greeting_node(state):
    user_input = state['user_input']

    prompt = f"""
you are a friendly AI assistant.

Reply politely to the following greeting.

Greeting:
{user_input}

keep the response under 20 words


"""
    response = llm.invoke(prompt)

    return {
        "response":response.content
    }