from typing import List, Any

from db.unit_of_work import UnitOfWork
from models.analytics_data import AnalyticsData
from models.enums import ExerciseType
from utility.utility import from_url_to_exercise


def analyse_grammar_exercise(all_answers_list: List[AnalyticsData]):
    if len(all_answers_list) == 0:
        return

    # Creo tanti dizionari quante sono le domande dell'esercizio
    count_sentences = len(all_answers_list[0].get_exercise_input().split("|")) - 1
    dict_list = [dict() for x in range(count_sentences)]

    for current_user in all_answers_list:
        # Divido le risposte per ogni utente
        user_answers = current_user.get_exercise_input()[1:].split("|")
        dictionary_index: int = 0
        for item in user_answers:
            # Inserisco la frase nel dizionario di tutte le risposte che sono state date.
            # Se la frase è già presente incremento il contatore.
            # Se la frase non è presente la aggiungo
            if item in dict_list[dictionary_index]:
                dict_list[dictionary_index][item] += 1
            else:
                dict_list[dictionary_index][item] = 1
            dictionary_index += 1

    # Ordino per le risposte date
    for item in dict_list:
        total = sum(item.values())
        sorted_dictionary: List[Any] = sorted(item.items(), key=lambda kv: kv[1])
        sorted_dictionary.reverse()

        print(sorted_dictionary)

    print("end analyse {0}".format(all_answers_list[0].get_url()))


if __name__ == '__main__':
    unit_of_work: UnitOfWork = UnitOfWork()
    unit_of_work.get_all_row(20)

    all_exercises: List[str] = unit_of_work.get_all_exercise_url()

    for exercise_url in all_exercises:
        answers: List[AnalyticsData] = unit_of_work.get_answers_exercise(exercise_url)
        exercise_type: ExerciseType = from_url_to_exercise(exercise_url)
        if exercise_type == ExerciseType.grammar_fill_the_blank:
            analyse_grammar_exercise(answers)

    print("End")
