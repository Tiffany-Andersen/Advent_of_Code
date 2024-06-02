# part 1

f = open('Day2input.txt', 'r')

line_number = 0
colors = ["red", "green", "blue"]
total = 0

while True:
    line = f.readline()
    line_number += 1
    if not line: 
        break

    words = line.split()
    flag = -1

    for index, word in enumerate(words):
        # print("current word: " , word)
        if word.isdigit() and len(words) > index + 1:
	        next_word = words[index + 1]
	        # print("next word: ", next_word)
	        if "red" in next_word and int(word) > 12:
	            flag = 1
	            break
	        if "green" in next_word and int(word) > 13:
	        	flag = 1
	        	break
	        if "blue" in next_word and int(word) > 14:
	        	flag = 1
	        	break
    # print(flag)
    if flag < 0:
        total = total + line_number
    flag = -1
    

print(total)



# part 2

f = open('Day2input.txt', 'r')

line_number = 0

power = 0

while True:
    line = f.readline()
    line_number += 1
    if not line: 
        break

    max_green = 0
    max_red = 0
    max_blue = 0

    words = line.split()

    for index, word in enumerate(words):
        
        # print("current word: " , word)
        if word.isdigit() and len(words) > index + 1:
	        next_word = words[index + 1]
	        # rint("next word: ", next_word)
	        if "red" in next_word and int(word) > max_red:
	            max_red = int(word)
	            
	        if "green" in next_word and int(word) > max_green:
	        	max_green = int(word)
	        	
	        if "blue" in next_word and int(word) > max_blue:
	        	max_blue = int(word)
	        	
        # print("min red: " , min_red)  
        # print("min_green: ", min_green) 
        # print("min blue: ", min_blue)	
	    
    power += (max_blue * max_green * max_red)
    
    

print(power)
    

    



# 12 red cubes, 13 green cubes, and 14 blue cubes