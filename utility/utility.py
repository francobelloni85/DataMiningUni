from models.enums import ExerciseType


def from_url_to_exercise(url: str):

    if url.startswith('https://www.esercizinglese.com/lezioni-inglesi/esercizi'):
        return ExerciseType.grammar_fill_the_blank

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





