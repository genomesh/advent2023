import numpy as np

file = open("input.txt", "r")

nodes = {}
instructions = ''
len_instructions = 0
start_locations = []
end_locations = []

for line in file.readlines():
    if '=' in line:
        l = line.split(' ')
        this_node = l[0]
        if this_node[2] == 'A':
            start_locations.append(this_node)
        if this_node[2] == 'Z':
            end_locations.append(this_node)
        left = l[2][1:4]
        right = l[3][0:3]
        nodes[this_node] = {'L': left, 'R': right}
    elif 'L' in line:
        instructions = line.strip()
        len_instructions = len(instructions)

locations = start_locations
print(f'{len(locations)} start locations')

def at_end_locations(locations):
    for location in locations:
        if location not in end_locations:
            return False
    return True

number_of_moves = 0
instruction_num = 0

while not at_end_locations(locations):
    instruction = instructions[instruction_num]
    locations = [nodes[location][instruction] for location in locations]
    number_of_moves += 1
    instruction_num = (instruction_num + 1) % len_instructions
    if number_of_moves % 1000000 == 0:
        print(number_of_moves)

print(f'answer: {number_of_moves}')

file.close()

#strategy: try to identify cycles
# 