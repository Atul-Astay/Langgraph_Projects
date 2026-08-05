from database.crud import (
    get_or_create_user,
    update_profile_from_schema,
)


def save_profile(db, user_id: str, profile):
    """
    Save the extracted profile into the database.

    Parameters
    ----------
    db : SQLAlchemy Session
    user_id : str
        Unique user identifier.
    profile : UserProfileSchema
        Structured profile extracted by the LLM.
    """

    if profile is None:
        return

    user = get_or_create_user(db, user_id)

    update_profile_from_schema(
        db=db,
        user=user,
        profile=profile,
    )


def profile_to_text(user) -> str:
    """
    Convert the stored profile into text that can be injected
    into the system prompt for personalization.
    """

    if user is None:
        return "No profile available."

    profile_lines = []

    if user.name:
        profile_lines.append(f"Name: {user.name}")

    if user.age is not None:
        profile_lines.append(f"Age: {user.age}")

    if user.height is not None:
        profile_lines.append(f"Height: {user.height} cm")

    if user.weight is not None:
        profile_lines.append(f"Weight: {user.weight} kg")

    if user.goal:
        profile_lines.append(f"Goal: {user.goal}")

    if user.level:
        profile_lines.append(f"Fitness Level: {user.level}")

    if not profile_lines:
        return "No profile available."

    return "\n".join(profile_lines)