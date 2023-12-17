file = open("input.txt", "r")

answer = 0

def check_game(reveals):
    min_cubes = {
        'blue': 0,
        'red': 0,
        'green': 0
    }
    for reveal in [r.strip() for r in reveals.replace(';', ',').split(',')]:
        num, colour = reveal.split(' ')
        min_cubes[colour] = max(int(num), min_cubes[colour])
            
    return min_cubes['blue'] * min_cubes['red'] * min_cubes['green']

for line in file.readlines():

    reveals = line.split(':')[1]
    answer += check_game(reveals)
        
    
print(answer)
file.close()