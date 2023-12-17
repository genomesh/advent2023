import numpy as np

file = open("test.txt", "r")

lines = file.readlines()

height = len(lines)
width = len(lines[0].strip())

is_adjacent = np.zeros((width, height), dtype=int)

num_gears = 0

for y, line in enumerate(lines):
    for x, symbol in enumerate(line.strip()):
        if symbol == '*':
            num_gears += 1
            is_adjacent[y-1:y+2, x-1:x+2] = num_gears

print(is_adjacent)

gear_adjacent_numbers = {(gear_id + 1): [] for gear_id in range(num_gears)}

for y, line in enumerate(lines):
    is_included = False
    cur_num = 0
    adj_gear_id = 0 # potentially one number is adjacent to multiple gears?
    for x, symbol in enumerate(line.strip()):
        if symbol.isnumeric():
            cur_num = cur_num * 10 + int(symbol)
            if is_adjacent[y, x]:
                is_included = True
                adj_gear_id = is_adjacent[y, x]
        else:
            if is_included:
                gear_adjacent_numbers[adj_gear_id].append(cur_num)
            cur_num = 0
            is_included = False
    if is_included:
        gear_adjacent_numbers[adj_gear_id].append(cur_num)

print(gear_adjacent_numbers)

answer = sum((adj_nums[0] * adj_nums[1] for adj_nums in gear_adjacent_numbers.values() if len(adj_nums) == 2))

print(answer)
file.close()