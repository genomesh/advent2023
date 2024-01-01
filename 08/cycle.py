#!/usr/bin/python3

from math import lcm

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

cycle_lengths = []

for start_location in start_locations:
    move_log = [[] for _ in instructions]
    num_moves = 0
    instruction_num = 0
    print(f'\nstart location: {start_location}')
    location = start_location
    move_log[0].append(location)
    num_ends = 0

    while location not in move_log[instruction_num][:-1]:
        instruction = instructions[instruction_num]
        location = nodes[location][instruction]
        if location[2] == 'Z':
            num_ends += 1
            print(f'at end point {location}, instruction {instruction_num}, cycle {len(move_log[instruction_num])}')
        instruction_num = (instruction_num + 1) % len_instructions
        move_log[instruction_num].append(location)
    print(f'instruction number: {instruction_num}')
    print(f'repeated location:{location}')
    cycle_start = move_log[instruction_num].index(location)
    cycle_end = len(move_log[instruction_num]) - 1
    print(f'cycle start: {cycle_start}')
    print(f'cycle end: {cycle_end}')
    cycle_length = cycle_end - cycle_start
    cycle_lengths.append(cycle_length)
    print(f'cycle length: {cycle_length}')
    print(f'number of ends: {num_ends}')

print('\ncycle lengths:')
print(cycle_lengths)

final_cycle = lcm(*cycle_lengths)

print(f'lowest common multiple: {final_cycle}')

print(f'answer: {final_cycle * 263}')

# cycle start
# cycle length (n * 263)
# times at which at end point.

file.close()

#strategy: try to identify cycles
# answer >= 2,900,000,000
# answer =  13,740,108,158,591