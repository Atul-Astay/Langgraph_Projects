from langchain_core.tools import tool


@tool
def calculate_bmi(weight: float, height: float) -> str:
    """
    Calculate Body Mass Index (BMI).

    Height must be in centimeters.
    Weight must be in kilograms.
    """

    height_m = height / 100

    bmi = weight / (height_m ** 2)

    category = ""

    if bmi < 18.5:
        category = "Underweight"

    elif bmi < 25:
        category = "Normal"

    elif bmi < 30:
        category = "Overweight"

    else:
        category = "Obese"

    return f"BMI: {bmi:.2f} ({category})"


@tool
def calculate_calories(
    weight: float,
    height: float,
    age: int,
) -> str:
    """
    Calculate estimated maintenance calories.
    """

    calories = (
        10 * weight
        + 6.25 * height
        - 5 * age
        + 5
    )

    return f"Estimated daily calories: {int(calories)} kcal"


@tool
def protein_requirement(weight: float) -> str:
    """
    Calculate daily protein requirement.
    """

    protein = weight * 1.8

    return f"Recommended protein intake: {protein:.1f} g/day"


@tool
def water_requirement(weight: float) -> str:
    """
    Calculate daily water intake.
    """

    water = weight * 35

    return f"Recommended water intake: {water:.0f} ml/day"


@tool
def beginner_workout(goal: str) -> str:
    """
    Return a beginner workout plan.
    """

    goal = goal.lower()

    if "fat" in goal:

        return """
Monday
- Walking 30 min
- Squats
- Pushups

Tuesday
- Cycling

Wednesday
- Lunges
"""

    if "muscle" in goal:

        return """
Monday
Chest

Tuesday
Back

Wednesday
Legs
"""

    return """
30 minutes walking

Pushups

Squats

Stretching
"""