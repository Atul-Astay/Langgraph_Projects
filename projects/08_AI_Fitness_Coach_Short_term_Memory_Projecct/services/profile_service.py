from sqlalchemy.orm import Session

from database.crud import (
    get_or_create_user,
    update_user,
)


def save_profile(
    db: Session,
    user_id: str,
    profile,
):

    user = get_or_create_user(
        db,
        user_id,
    )

    update_user(
        db,
        user,
        name=profile.name,
        age=profile.age,
        height=profile.height,
        weight=profile.weight,
        goal=profile.goal,
        level=profile.level,
    )

    return user