from langchain_groq import ChatGroq
from dotenv import load_dotenv
from schemas.profile import UserProfileSchema

load_dotenv()

MODEL = "llama-3.3-70b-versatile"

profile_llm = ChatGroq(
    model=MODEL,
    temperature=0,
)

workout_llm = ChatGroq(
    model=MODEL,
    temperature=0.3,
)

diet_llm = ChatGroq(
    model=MODEL,
    temperature=0.2,
)

coach_llm = ChatGroq(
    model=MODEL,
    temperature=0.5,
)

profile_extractor = profile_llm.with_structured_output(
    UserProfileSchema
)