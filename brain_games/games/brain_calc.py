from random import randint, choice


GAME_RULES = 'What is the result of the expression?'
OPERATORS = ("+", "-", "*")
MIN_RANDOM_NUMBER = 0
MAX_RANDOM_NUMBER = 100


def generate_random_number():
    number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    return number


def calculate_expression(number1, number2, operator):
    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2


def make_task():
    number1 = generate_random_number()
    number2 = generate_random_number()
    operator = choice(OPERATORS)
    answer = calculate_expression(number1, number2, operator)
    question = f'{number1} {operator} {number2}'
    return (question, answer)
