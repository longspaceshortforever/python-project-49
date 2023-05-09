import prompt


ROUNDS = [1, 2, 3]


def welcome_user():
    print("Welcome to the Brain Games!")


def get_user_name():
    return prompt.string('May I have your name? ')


def get_user_answer():
    return prompt.string("Your answer: ")


def check_number_is_even(number):
    if number % 2 != 0:
        return False
    return True


def generate_wrong_message(user_answer, correct_answer, user_name):
    wrong_msg = "\"" + f'{user_answer}' + "\" is wrong answer ;(. "
    correct_msg = "Correct answer was \"" + f'{correct_answer}' + "\"."
    advice = "\nLet's try again, " + f'{user_name}' + "!"
    wrong_answer_msg = wrong_msg + correct_msg + advice
    print(wrong_answer_msg)


def run_game_engine(game):
    answers = 0
    
    welcome_user()
    user_name = get_user_name()
    print("Hello, " + f'{user_name}')
    print(game.GAME_RULES)
    
    for _ in ROUNDS:
        
        question = game.make_question()
        print("Question: " + f'{question}')
        correct_answer = game.get_correct_answer(question)
        user_answer = get_user_answer()
        if user_answer == correct_answer:
            print("Correct!")
            answers = answers + 1
            
        else:
            generate_wrong_message(user_answer, correct_answer, user_name)
            break
        
    if answers == 3:
        print("Congratulation, " + f'{user_name}' + "!")
        