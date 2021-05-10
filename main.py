import string
from typing import List, Any

from db.unit_of_work import UnitOfWork
from models.analytics_data import AnalyticsData
from models.enums import ExerciseType
from models.feedback_exercise_data import ExerciseFeedbackData
from utility.utility import from_url_to_exercise, get_unit_and_exercise_from_url
import jellyfish

exclude_punctuation = (set(string.punctuation))
exclude_punctuation.discard("'")

def analyse_grammar_exercise(my_unit_of_work: UnitOfWork, all_answers_list: List[AnalyticsData]):
    """
    Questo [lungo!] metodo prende la lista di tutte le risposte date dagli utenti
     per una data risposta per l'esercizio di grammatica.
    Poi raggruppa le risposte date e le conta.
    Infine salva quelle che hanno avuto una maggiore frequenza.
    :param my_unit_of_work:
    :param all_answers_list:
    :return:
    """

    if len(all_answers_list) == 0:
        return

    url = all_answers_list[0].get_url()

    # 1 - creo tanti dizionari quante sono le domande dell'esercizio
    count_sentences = len(all_answers_list[0].get_exercise_input().split("|")) - 1
    dict_list = [dict() for x in range(count_sentences)]

    for current_user in all_answers_list:
        # Divido le risposte per ogni utente
        user_answers = current_user.get_exercise_input()[1:].strip().split("|")
        dictionary_index: int = 0
        for item in user_answers:
            trim_user_answer = item.strip()
            clean_user_answer = ''.join(ch for ch in trim_user_answer if ch not in exclude_punctuation)

            if trim_user_answer != clean_user_answer:
                print("trim_user_answer= {0} - clean_user_answer={1}".format(trim_user_answer, clean_user_answer))

            if dictionary_index < len(dict_list):
                # Inserisco la frase nel dizionario di tutte le risposte che sono state date.
                # Se la frase è già presente incremento il contatore.
                # Se la frase non è presente la aggiungo
                if clean_user_answer in dict_list[dictionary_index]:
                    dict_list[dictionary_index][clean_user_answer] += 1
                else:
                    dict_list[dictionary_index][clean_user_answer] = 1
                dictionary_index += 1
            else:
                print("Something went wrong")

    # Da url ad unita ed esercizio
    exercises_info = get_unit_and_exercise_from_url(exercise_type.grammar_fill_the_blank, url)
    unit: int = exercises_info[0]
    exercise: int = exercises_info[1]

    # 2 - Get the solutions
    solutions: List = unit_of_work.get_grammar_solution(unit, exercise)
    # Remove the first sentence (example)
    del solutions[0]
    exercise_id: int = solutions[0][0]
    sentence: int = 1
    solution_index = 0

    # 3 - salvo le risposte che gli utenti hanno dato alle varie frasi dell'esercizio
    for item in dict_list:
        total = sum(item.values())
        if total != len(all_answers_list):
            raise Exception("Mismatch between the number of total exercises")

        sorted_dictionary: List[Any] = sorted(item.items(), key=lambda kv: kv[1])
        sorted_dictionary.reverse()

        list_to_save: List[ExerciseFeedbackData] = []
        count_answer_to_save: int = 0

        answer_number: int = 1

        for i in range(len(sorted_dictionary)):
            sentence_solution_1: str = solutions[solution_index][1]
            sentence_solution = ''.join(ch for ch in sentence_solution_1 if ch not in exclude_punctuation)
            if sentence_solution_1 != sentence_solution:
                print("sentence_solution_1= {0} - sentence_solution={1}".format(sentence_solution_1, sentence_solution))

            # Add the right answer as first row
            if i == 0:
                solution: ExerciseFeedbackData = ExerciseFeedbackData(ExerciseType.grammar_fill_the_blank, exercise_id, sentence, i, sentence_solution, 100, "")
                list_to_save.append(solution)

            answer = sorted_dictionary[i][0].strip()
            count_answer_made: int = sorted_dictionary[i][1]
            percent_answer_made: int = int((count_answer_made * 100) / total)

            # Skip the empty answer
            if len(answer) == 0:
                continue

            correction: str = ""
            if jellyfish.hamming_distance(sentence_solution, answer) == 1 and len(sentence_solution) >= 3:
                correction = "typo?"

            if percent_answer_made > 2 or count_answer_to_save <= 3:
                t: ExerciseFeedbackData = ExerciseFeedbackData(ExerciseType.grammar_fill_the_blank, exercise_id, sentence, answer_number, answer, percent_answer_made, correction)
                list_to_save.append(t)
                count_answer_to_save += 1
                answer_number += 1
                if count_answer_to_save >= 10:
                    break
            else:
                break

        if my_unit_of_work.save_exercise_feedback(list_to_save):
            print("Insert exercise {0}= {1}".format(exercise_id, sorted_dictionary))
        else:
            print("Fail to insert exercise {0}= {1}".format(exercise_id, sorted_dictionary))

        # Incremento i contatori delle frasi
        sentence += 1
        solution_index += 1

    print("end analyse {0}".format(all_answers_list[0].get_url()))


if __name__ == '__main__':
    unit_of_work: UnitOfWork = UnitOfWork()
    unit_of_work.get_all_row(20)

    all_exercises: List[str] = unit_of_work.get_all_exercise_url()

    for exercise_url in all_exercises:
        answers: List[AnalyticsData] = unit_of_work.get_answers_exercise(exercise_url)
        exercise_type: ExerciseType = from_url_to_exercise(exercise_url)
        if exercise_type == ExerciseType.grammar_fill_the_blank:
            analyse_grammar_exercise(unit_of_work, answers)

    print("End")
