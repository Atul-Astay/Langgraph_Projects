from typing import Optional

from pydantic import BaseModel, Field


class UserProfileSchema(BaseModel):

    name: Optional[str] = Field(default=None)

    age: Optional[int] = Field(default=None)

    height: Optional[float] = Field(default=None)

    weight: Optional[float] = Field(default=None)

    goal: Optional[str] = Field(default=None)

    level: Optional[str] = Field(default=None)