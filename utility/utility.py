from typing import List, Any

from models.enums import ExerciseType


def from_url_to_exercise(url: str):
    if url.startswith('https://www.esercizinglese.com/lezioni-inglesi/esercizi/'):
        return ExerciseType.grammar_fill_the_blank

    if url.startswith('https://www.esercizinglese.com/lezioni-inglesi/esercizi-crocette/'):
        return ExerciseType.grammar_multiple_choose

    if url.startswith('https://www.esercizinglese.com/traduzioni/brani-facili/esercizi'):
        return ExerciseType.translate_easy

    if url.startswith("https://www.esercizinglese.com/traduzioni/pet/esercizi"):
        return ExerciseType.translate_pet

    if url.startswith("https://www.esercizinglese.com/traduzioni/testi-in-inglese/esercizi"):
        return ExerciseType.translate_text

    if url.startswith("https://www.esercizinglese.com/audio/libri/esercizi"):
        return ExerciseType.translate_audio

    if url.startswith("https://www.esercizinglese.com/esercizi-facili/esercizi"):
        return ExerciseType.easy_fill_the_blank


def get_unit_and_exercise_from_url(exercise_type: ExerciseType, url: str) -> List[Any]:
    result: List = []
    if exercise_type == ExerciseType.grammar_fill_the_blank:
        temp = url.split('/')
        unit = temp[5]
        exercise = temp[6]
        result.append(unit)
        result.append(exercise)

    return result
