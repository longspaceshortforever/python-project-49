from .engine import welcome_user, generate_number
import prompt

COUNT_OF_CORRECT_ANSWERS = 3
GAMES_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_even():
    welcome_user()
    print(GAMES_RULES)
    CURRENT_NUMBER = generate_number
    