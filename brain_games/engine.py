import prompt


ROUNDS = [1, 2, 3]


def generate_wrong_message(user_answer, correct_answer, user_name):
    wrong_answer_msg = f'"{user_answer}" is wrong answer ;(. ' + \
        f'Correct answer was "{correct_answer}".' + \
        f'\nLet\'s try again, {user_name}!'
    print(wrong_answer_msg)


def run_game_engine(game):
    answers = 0
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULES)

    for _ in ROUNDS:
        question_and_answer = game.make_task()
        question = question_and_answer[0]
        correct_answer = str(question_and_answer[1])
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:

            print("Correct!")
            answers = answers + 1
        else:
            generate_wrong_message(user_answer, correct_answer, user_name)
            break

    if answers == 3:
        print(f'Congratulations, {user_name}!')
