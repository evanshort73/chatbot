import editdistance
import random

with open("dialog.txt") as f:
    dialog = list(line.rstrip("\n") for line in f)

dialog = [(x, bool(dialog[i + 1])) for i, x in enumerate(dialog) if x]

def weighted_random_index(weights):
    sample = sum(weights) * random.random()
    total = 0
    for i, weight in enumerate(weights):
        total += weight
        if total >= sample:
            return i

def score_to_probability(score):
    BASE = 10.0
    return BASE ** -score

def get_line_probability(user_input, line, good):
    if good:
        return score_to_probability(editdistance.eval(user_input,
                                                      line.lower()))
    return 0.0

user_input = "dummy"
while user_input:
    possible_responses = []
    total_probability = 0
    user_input = raw_input('say something: ').lower()
    response = ""
    weights = [get_line_probability(user_input, line, good) \
               for line, good in dialog]
    selected_index = weighted_random_index(weights)
    response, _ = dialog[selected_index + 1]
    score = editdistance.eval(user_input, response.lower())
    print 'bot response: ', response
    print '( score: ', score, ')'
    print '__________________________'
