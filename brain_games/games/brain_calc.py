from random import randint


GAME_RULES = 'What is the result of the expression?'
OPERATORS = ("+", "-", "*")
MIN_RANDOM_NUMBER = 0
MAX_RANDOM_NUMBER = 100


def generate_random_number():
    number = randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    return number


def generate_random_operator():
    index = randint(0, 2)
    operator = OPERATORS[index]
    return operator


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
    operator = generate_random_operator()
    answer = calculate_expression(number1, number2, operator)
    question = f'{number1} {operator} {number2}'
    return (question, answer)
