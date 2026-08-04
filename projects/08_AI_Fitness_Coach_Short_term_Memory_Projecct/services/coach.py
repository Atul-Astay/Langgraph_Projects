import re

from sqlalchemy.orm import Session

from database.crud import get_or_create_user, update_user


def save_profile(db: Session, user_id: str, message: str):

    user = get_or_create_user(db, user_id)

    name = re.search(r"my name is (\w+)", message, re.I)
    weight = re.search(r"(\d+)\s*kg", message, re.I)
    age = re.search(r"i am (\d+)", message, re.I)

    goal = None

    if "fat loss" in message.lower():
        goal = "Fat Loss"

    elif "weight loss" in message.lower():
        goal = "Weight Loss"

    elif "muscle gain" in message.lower():
        goal = "Muscle Gain"

    update_user(
        db,
        user,
        name=name.group(1) if name else None,
        age=int(age.group(1)) if age else None,
        weight=float(weight.group(1)) if weight else None,
        goal=goal,
    )


def profile_to_text(user):

    return f"""
Name: {user.name}
Age: {user.age}
Height: {user.height}
Weight: {user.weight}
Goal: {user.goal}
Level: {user.level}
"""