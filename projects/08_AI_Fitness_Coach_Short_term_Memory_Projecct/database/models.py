from sqlalchemy import Column, Integer, Float, String

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