from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_random_number():
    return randint(0, 100)


def make_question():
    random_number = generate_random_number()
    return random_number


def get_correct_answer(question):
    if question % 2 == 0:
        return "yes"
    return "no"
