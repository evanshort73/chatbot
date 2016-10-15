import editdistance

with open("dialog.txt") as f:
    dialog = list(line.rstrip("\n") for line in f)

user_input = "dummy"
while user_input:
    user_input = raw_input().lower()
    response = ""
    for i, line in enumerate(dialog):
        score = editdistance.eval(user_input, line.lower())
        if not response or score < best_score:
            response = dialog[(i+1) % len(dialog)]
            best_score = score
    print response
    print best_score
