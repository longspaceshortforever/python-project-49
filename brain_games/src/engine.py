import prompt
from random import randint 

def welcome_user():
    """Greeting user and gives name"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))

def generate_number():
    """Generate random integral number"""
    RANDOM_NUMBER = randint(0, 100)
    print(RANDOM_NUMBER)