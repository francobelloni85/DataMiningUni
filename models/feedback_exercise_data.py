import dataclasses

from models.enums import ExerciseType


@dataclasses
class ExerciseFeedbackData:
    exercise_type: ExerciseType
    exercise_id: int
    question_number: int
    answer: int
    percentage: int
    correction: str
