file = open("input.txt", "r")

answer = 0

for line in file.readlines():
    a, b, c = line.replace(':', '|').split('|')
    winning_numbers = [int(num) for num in filter(None, b.split(' '))]
    our_numbers = [int(num) for num in filter(None, c.split(' '))]
    overlap = [number for number in our_numbers if number in winning_numbers]
    if (len(overlap) > 0):
        answer += 2 ** (len(overlap) - 1)


print(answer)
file.close()