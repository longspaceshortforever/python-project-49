import prompt
from random import randint


def welcome_user():
    """Greeting user and gives name"""
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    return user_name


def generate_number():
    """Generate random integral number"""
    random_number = randint(0, 100)
    return random_number


def check_number_is_even(number):
    if number % 2 != 0:
        return False
    return True
