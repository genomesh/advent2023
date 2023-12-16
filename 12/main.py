file = open("input.txt", "r")

total = 0

for line_number, line in enumerate(file.readlines()):

    print(line_number)

    row_possibilities = 1
    
    layout, actual_damaged = line.split()
    #print(layout)
    actual_damaged = list(map(int, actual_damaged.split(',')))
    #print(list(actual_damaged))

    def is_valid(config):
        
        # want to get back e.g.
        # 2, 3, 2+
        # then match with
        # 2, 3, 1, 1
        # to get an error as 2+ > 1

        cur_damaged = [0]

        for symbol in config:
            if symbol == '?':
                break
            if symbol == '.':
                cur_damaged.append(0)
            if symbol == '#':
                cur_damaged[-1] += 1
        
        cur_damaged = [x for x in cur_damaged if x != 0]

        #print(cur_damaged)

        if len(cur_damaged) == 0:
            return True
        
        if len(cur_damaged) > len(actual_damaged):
            return False

        for i, d in enumerate(cur_damaged):
            if actual_damaged[i] < d:
                return False

        return True
    
    def is_exact(config):
        
        # now the config has no ?
        # check if damaged springs match exactly.

        cur_damaged = [0]

        for symbol in config:
            if symbol == '?':
                break
            if symbol == '.':
                cur_damaged.append(0)
            if symbol == '#':
                cur_damaged[-1] += 1
        
        cur_damaged = list([x for x in cur_damaged if x != 0])

        #print(cur_damaged)

        if len(cur_damaged) != len(actual_damaged):
            return False

        for i in range(len(cur_damaged)):
            if cur_damaged[i] != actual_damaged[i]:
                return False

        return True
        
    def find_recursive(current_config):
        if not is_valid(current_config):
            return 0
        if current_config.count('?') == 0:
            return int(is_exact(current_config))
        damaged_possibilites = find_recursive(current_config.replace('?', '#', 1))
        working_possibilites = find_recursive(current_config.replace('?', '.', 1))
        total_possibilites = damaged_possibilites + working_possibilites
        #print(current_config)
        #print(total_possibilites)
        return total_possibilites

    line_possibilities = find_recursive(layout)
    total += line_possibilities
    
    
# can do recursively.
# is DP better?

print(total)
    
file.close()