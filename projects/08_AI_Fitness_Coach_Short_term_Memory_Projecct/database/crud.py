from sqlalchemy.orm import Session

from .models import UserProfile


def get_user(db: Session, user_id: str):
    return (
        db.query(UserProfile)
        .filter(UserProfile.user_id == user_id)
        .first()
    )


def create_user(db: Session, user_id: str):
    user = UserProfile(user_id=user_id)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_or_create_user(db: Session, user_id: str):

    user = get_user(db, user_id)

    if user:
        return user

    return create_user(db, user_id)


def update_user(
    db: Session,
    user: UserProfile,
    **kwargs,
):

    for key, value in kwargs.items():

        if value is not None:
            setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user 

def update_profile_from_schema(
    db,
    user,
    profile,
):

    data = profile.model_dump(exclude_none=True)

    for key, value in data.items():
        setattr(user, key, value)

    db.commit()

    db.refresh(user)

    return user