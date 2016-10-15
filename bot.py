import editdistance
import itertools

with open("dialog.txt") as f:
    dialog = list(line.rstrip("\n") for line in f)

dialog = [(x, bool(dialog[i + 1])) for i, x in enumerate(dialog) if x]

user_input = "dummy"
while user_input:
    user_input = raw_input('say something: ').lower()
    response = ""
    for i, (line, good) in enumerate(dialog):
        if good:
            score = editdistance.eval(user_input, line.lower())
            if not response or score < best_score:
                response, _ = dialog[i + 1]
                best_score = score
    print 'bot response: ', response
    print '( score: ', best_score, ')'
    print '__________________________'
