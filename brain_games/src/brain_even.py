from .engine import welcome_user, generate_number, check_number_is_even
import prompt


COUNT_OF_CORRECT_ANSWERS = 0
GAMES_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_count_of_answers():
    global COUNT_OF_CORRECT_ANSWERS
    if COUNT_OF_CORRECT_ANSWERS == 3:
        print("Congratulations, Bill!")


def iterate_game_even():
    """Realize one cycle of game"""
    global COUNT_OF_CORRECT_ANSWERS
    if COUNT_OF_CORRECT_ANSWERS < 3:
        current_number = generate_number()
        correct_answer = "no"

        if check_number_is_even(current_number):
            correct_answer = "yes"

        question = "Question: " + f'{current_number}' + "\n" + "Your answer: "
        answer = prompt.string(question)

        if correct_answer == answer:
            print("Correct!")
            COUNT_OF_CORRECT_ANSWERS = COUNT_OF_CORRECT_ANSWERS + 1
            check_count_of_answers()
            iterate_game_even()
        else:
            wrong_answer_message = "\"" + f'{answer}' + "\" is wrong answer ;(."
            correct_answer_message = "Correct answer was \"" + f'{correct_answer}' + "\"."
            advice = "\nLet's try again, Bill!"
            wrong_message = what_is_wrong_answer + what_is_correct_answer + what_to_do
            print(wrong_message)


def game_even():
    welcome_user()
    print(GAMES_RULES)
    iterate_game_even()
