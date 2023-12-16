file = open("input.txt", "r")

calibration_sum = 0

digits3 = {
    'one': 1,
    'two': 2,
    'six': 6
}

digits4 = {
    'four': 4,
    'five': 5,
    'nine': 9
}

digits5 = {
    'three': 3,
    'seven': 7,
    'eight': 8
}

for line in file.readlines():
    #print(line)
    i = 0
    while not line[i].isnumeric():
        if line[i:i+3] in digits3.keys():
            calibration_sum += 10 * digits3[line[i:i+3]]
            break

        elif line[i:i+4] in digits4.keys():
            calibration_sum += 10 * digits4[line[i:i+4]]
            break

        elif line[i:i+5] in digits5.keys():
            calibration_sum += 10 * digits5[line[i:i+5]]
            break

        else:
            i += 1

    if line[i].isnumeric():
        calibration_sum += 10 * int(line[i])

    i = len(line) - 1
    while not line[i].isnumeric():
        if line[i-3:i] in digits3.keys():
            calibration_sum += digits3[line[i-3:i]]
            break

        elif line[i-4:i] in digits4.keys():
            calibration_sum += digits4[line[i-4:i]]
            break

        elif line[i-5:i] in digits5.keys():
            calibration_sum += digits5[line[i-5:i]]
            break

        else:
            i -= 1

    if line[i].isnumeric():
        calibration_sum += int(line[i])
    
print(calibration_sum)
    
file.close()