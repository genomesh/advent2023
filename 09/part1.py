file = open('test.txt', 'r')

def all_zero(array):
    for a in array:
        if a != 0:
            return False
    return True

answer = 0

for line in file.readlines():
    seq = [int(num) for num in line.split(' ')]
    print(seq)
    levels = [seq.copy()]
    while not all_zero(levels[-1]):
        levels.append([levels[-1][i+1] - levels[-1][i] for i in range(len(levels[-1])-1)])
    print(levels)
    row_answer = 0
    for level in reversed(levels):
        row_answer = row_answer + level[-1]
        print(level[-1])
    print(f'row answer: {row_answer}')
    answer += row_answer

print(f'answer: {answer}')