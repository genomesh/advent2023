file = open("input.txt", "r")

times = []
record_distances = []

def parse_line(line):
    return int(
        "".join(
        map(lambda x: x.strip(),
        filter(lambda x: x.strip() != '',
        line.split(' ')[1:]
    ))))

time, record_distance = map(parse_line, file.readlines())

ways_to_win = 0

smallest_time_held = 0
largest_time_held = time

while smallest_time_held * (time - smallest_time_held) <= record_distance:
    smallest_time_held += 1

while largest_time_held * (time - largest_time_held) <= record_distance:
    largest_time_held -= 1

print(largest_time_held - smallest_time_held + 1)

file.close()