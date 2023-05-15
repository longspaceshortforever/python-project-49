from random import randint
from math import gcd


GAME_RULES = 'Find the greatest common divisor of given numbers.'
MIN_RANDOM_NUMBER = 0
MAX_RANDOM_NUMBER = 100


def generate_random_number():
    return randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)


def make_task():
    number1 = generate_random_number()
    number2 = generate_random_number()
    numbers = f'{number1}' + " " + f'{number2}'
    question = numbers
    answer = get_correct_answer(number1, number2)
    return (question, answer)


def get_correct_answer(number1, number2):
    return gcd(number1, number2)
