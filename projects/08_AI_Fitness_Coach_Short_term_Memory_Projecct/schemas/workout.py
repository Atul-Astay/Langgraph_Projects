from datetime import date

from pydantic import BaseModel


class WorkoutRecord(BaseModel):

    workout_date: date

    workout_name: str

    duration: int

    calories: float

    status: str