file = open("input.txt", "r")

times = []
record_distances = []

def parse_line(line):
    return list(
        map(lambda x: int(x.strip()),
        filter(lambda x: x.strip() != '',
        line.split(' ')[1:]
    )))


times, record_distances = map(parse_line, file.readlines())

answer = 1

for time, record in zip(times, record_distances):
    ways_to_win = 0
    for time_held in range(1, time):
        distance = time_held * (time - time_held)
        if distance > record:
            ways_to_win += 1
    print(ways_to_win)
    answer *= ways_to_win

print(answer)

file.close()