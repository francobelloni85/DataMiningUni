from dataclasses import dataclass

from models.enums import ExerciseType


@dataclass
class ExerciseFeedbackData:
    exercise_type: ExerciseType
    exercise_id: int
    question_number: int
    answer_number: int
    answer: str
    percentage: int
    correction: str
