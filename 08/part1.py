import numpy as np

file = open("input.txt", "r")

nodes = {}
instructions = ''
len_instructions = 0
# is 263, which is prime

for line in file.readlines():
    if '=' in line:
        l = line.split(' ')
        this_node = l[0]
        left = l[2][1:4]
        right = l[3][0:3]
        nodes[this_node] = {'L': left, 'R': right}
    elif 'L' in line:
        instructions = line.strip()
        len_instructions = len(instructions)

location = 'AAA'
number_of_moves = 0
instruction_num = 0
while location != 'ZZZ':
    instruction = instructions[instruction_num]
    location = nodes[location][instruction]
    number_of_moves += 1
    instruction_num = (instruction_num + 1) % len_instructions

print(number_of_moves)

file.close()