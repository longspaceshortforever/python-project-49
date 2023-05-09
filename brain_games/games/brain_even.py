from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_random_number():
    return randint(0, 100)


def make_task():
    number = generate_random_number()
    question = number
    answer = get_correct_answer(number)
    return (question, answer)


def get_correct_answer(number):
    if number % 2 == 0:
        return "yes"
    return "no"
