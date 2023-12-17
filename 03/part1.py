import numpy as np

file = open("input.txt", "r")

answer = 0

lines = file.readlines()

height = len(lines)
width = len(lines[0].strip())

is_adjacent = np.zeros((width, height), dtype=int)

for y, line in enumerate(lines):
    for x, symbol in enumerate(line.strip()):
        if not symbol.isnumeric() and symbol != '.':
            is_adjacent[y-1:y+2, x-1:x+2] = 1

for y, line in enumerate(lines):
    is_included = 0
    cur_num = 0
    for x, symbol in enumerate(line.strip()):
        if symbol.isnumeric():
            cur_num = cur_num * 10 + int(symbol)
            if is_adjacent[y, x]:
                is_included = 1
        else:
            answer += cur_num * is_included
            cur_num = 0
            is_included = 0
    answer += cur_num * is_included
    cur_num = 0
    is_included = 0


print(answer)
file.close()