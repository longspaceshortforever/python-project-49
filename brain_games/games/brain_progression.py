from random import randint


GAME_RULES = 'What number is missing in the progression?'


def generate_start_number():
    return randint(0, 100)


def generate_step():
    return randint(1, 10)


def generate_progression_length():
    return randint(5, 20)


def generate_progression():
    start_number = generate_start_number()
    step = generate_step()
    last_index = generate_progression_length() + 1
    progression = [start_number]
    current_index = len(progression) - 1
    while len(progression) < last_index:
        progression.append(progression[current_index] + step)
        current_index = current_index + 1
    return progression


def replace_random_element(sequence):
    new_sequence = sequence[:]
    last_index = len(new_sequence) - 1
    random_index = randint(0, last_index)
    exluded_element = new_sequence.pop(random_index)
    new_sequence.insert(random_index, "..")
    return (new_sequence, exluded_element)


def make_sentence(sequence):
    sentence = ""
    for element in sequence:
        sentence += str(element) + " "
    return sentence


def make_task():
    progression = generate_progression()
    edited_progression_and_answer = replace_random_element(progression)
    edited_progression = edited_progression_and_answer[0]
    question = make_sentence(edited_progression)
    answer = edited_progression_and_answer[1]
    return (question, answer)
