import pdb

with open('dialog.txt', 'w+') as dialog_fd:
    with open('movie_lines.txt') as f:
        lines = f.readlines()
        for line in lines:
            dialog_fd.write(line.split('+++$+++')[-1].strip() + '\n')
