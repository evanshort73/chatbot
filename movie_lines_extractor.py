import pdb

DELIMETER = ' +++$+++ '
dialog_hash = {}

with open('movie_lines.txt') as f:
    for line in f:
        splitted_line = line.split(DELIMETER)
        line_number = splitted_line[0].strip()
        sentence = splitted_line[-1].strip()
        dialog_hash[line_number] = sentence

with open('dialog.txt', 'w+') as dialog_fd:
    with open('movie_conversations.txt') as f:
        for line in f:
            line_positions = eval(line.split(DELIMETER)[-1].strip())
            for line_position in line_positions:
                dialog_fd.write(dialog_hash[line_position] + '\n')
            dialog_fd.write('\n')
