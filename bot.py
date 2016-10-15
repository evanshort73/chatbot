import editdistance
import itertools
import random

with open("dialog.txt") as f:
    dialog = list(line.rstrip("\n") for line in f)

dialog = [(x, bool(dialog[i + 1])) for i, x in enumerate(dialog) if x]

def randomly_select_response(responses, total_probability):
    selected_prob = total_probability * random.random()
    sum_prob = 0
    for response in responses:
        sum_prob += response[1]
        if sum_prob >= selected_prob:
            return response

def generate_probability(score):
    BASE = 10.0
    return BASE ** -score

user_input = "dummy"
while user_input:
    possible_responses = []
    total_probability = 0
    user_input = raw_input('say something: ').lower()
    response = ""
    for i, (line, good) in enumerate(dialog):
        if good:
            score = editdistance.eval(user_input, line.lower())
            prob  = generate_probability(score)
            possible_responses.append((dialog[i+1][0], prob, score))
            total_probability += prob
    response, prob, score = randomly_select_response(possible_responses, total_probability)
    print 'bot response: ', response
    print '( score: ', score, ')'
    print '__________________________'
