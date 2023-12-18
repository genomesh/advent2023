import numpy as np

file = open("input.txt", "r")
lines = file.readlines()

answer = 0

num_copies = np.ones(len(lines), dtype=int)

for id, line in enumerate(lines):
    a, b, c = line.replace(':', '|').split('|')
    winning_numbers = [int(num) for num in filter(None, b.split(' '))]
    our_numbers = [int(num) for num in filter(None, c.split(' '))]
    overlap = len([number for number in our_numbers if number in winning_numbers])
    cur_copies = num_copies[id]
    answer += cur_copies
    num_copies[id + 1 : id + overlap + 1] += cur_copies


print(answer)
file.close()