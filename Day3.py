# part 1

import re

f = open('Day3input.txt', 'r')

chart = []
total = 0

# Read in all of the input to create a list of lines, stored in "chart"
while True:
    line = f.readline()
    if not line: 
        break
    chart.append(line)

symbols = ['/','$','=','!','@','#','&','%','^','*','-','+']
    
for index, line in enumerate(chart):
    
    # Find all numbers in the line
    matches = re.finditer(r'\d+', line)

    # Only check the next line for symbols if this is the first line in chart
    if index == 0:
        next_line = chart[1]
        for match in matches:
            # Store index of start of each number, and number itelf
            start_index = match.start()
            number = match.group()
            # Determine if number is adjacent to any symbol, including diagonally
            for symbol in symbols:
                if (
                    symbol in next_line[max(start_index - 1, 0) : min(start_index + len(number) + 1, len(next_line))] or 
                    (symbol in line[max(0, start_index - 1)] or symbol in line[min(start_index + len(number), len(line))])
                ):
                    total += int(number)
                    break

    elif index == len(chart) - 1:
        previous_line = chart[index - 1]
        for match in matches:
            start_index = match.start()
            number = match.group()
            for symbol in symbols:
                if (
                    symbol in previous_line[start_index - 1 : start_index + len(number) + 1] or 
                    (symbol in line[max(0, start_index - 1)] or symbol in line[min(start_index + len(number), len(line))])
                ):
                    total += int(number)
                    break
    else:
        next_line = chart[index + 1]
        previous_line = chart[index - 1]
        for match in matches:
            start_index = match.start()
            number = match.group()
            for symbol in symbols:
                if (
                    (symbol in next_line[max(start_index - 1, 0) : min(start_index + len(number) + 1, len(next_line))]) or 
                    (symbol in previous_line[start_index - 1 : start_index + len(number) + 1]) or 
                    (symbol in line[max(0, start_index - 1)] or symbol in line[min(start_index + len(number), len(line))])
                ):
                    total += int(number)
                    

print(total)


