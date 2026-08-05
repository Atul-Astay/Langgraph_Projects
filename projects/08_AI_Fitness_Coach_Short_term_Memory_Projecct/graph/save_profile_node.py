from database.database import SessionLocal

from services.profile_service import save_profile


def save_profile_node(state):

    db = SessionLocal()

    try:

        profile = state["profile_data"]

        user_id = state["user_id"]

        save_profile(
            db,
            user_id,
            profile,
        )

    finally:
        db.close()

    return {}