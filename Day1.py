f = open('Day1input.txt', 'r')

total = 0

while True:
    line = f.readline()
    if not line: 
        break
    for char in line:
        if char.isdigit():
            firstDigit = char
            break
    for char in reversed(line):
        if char.isdigit():
            lastDigit = char
            break
    coord = int(str(firstDigit) + str(lastDigit))  # Convert to strings before concatenation
    total += coord

print(total)


# Part 2:

f = open('Day1input.txt', 'r')

digit_strings = ["one", 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
total = 0
line_number = 0
firstDigit = -1
lastDigit = -1
while True:
    line = f.readline()
    # print("line number: ", line_number)
    line_number += 1
    if not line: 
        break
    
    for index, char in enumerate(line):
        # print("testing break")
        if int(firstDigit) > 0:
       	    break
        if char.isdigit():
            firstDigit = char
            # print("first digit: ", firstDigit)  
            break
        for digit_string in digit_strings:
            if line[index:index+len(digit_string)] == digit_string:
                # print("index: ", index)
                firstDigit = str(digit_strings.index(digit_string) + 1)
                # print("first digit: ", firstDigit)              
                break

    for index, char in enumerate(line):
        if char.isdigit():
            lastDigit = char
            # print("last digit: ", lastDigit)

        for digit_string in digit_strings:
            if line[index:index+len(digit_string)] == digit_string:
                lastDigit = str(digit_strings.index(digit_string) + 1)
                # print("last digit: ", lastDigit)
                

    coord = int(str(firstDigit) + str(lastDigit))
    # print("coordinate: ", coord)
    total += coord
    firstDigit = -1
    lastDigit = -1

print(total)

