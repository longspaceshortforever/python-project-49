from random import randint


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_random_number():
    return randint(0, 100)

def is_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if (k == 0):
        return True
    else:
        return False


def make_task():
    number = generate_random_number()
    question = number
    answer = get_correct_answer(number)
    return (question, answer)


def get_correct_answer(number):
    if is_prime(number):
        return "yes"
    else:
        return "no"