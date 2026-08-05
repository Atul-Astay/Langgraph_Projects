from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Date,
    ForeignKey,
)
from .database import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True)

    user_id = Column(String, unique=True, index=True)

    name = Column(String)

    age = Column(Integer)

    height = Column(Float)

    weight = Column(Float)

    goal = Column(String)

    level = Column(String)

class WorkoutHistory(Base):

    __tablename__ = "workout_history"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        String,
        ForeignKey("user_profiles.user_id")
    )

    workout_date = Column(Date)

    workout_name = Column(String)

    duration = Column(Integer)

    calories = Column(Float)

    status = Column(String)