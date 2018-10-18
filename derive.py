#Bryan Mejia-Medina
#CS 312 - Assignment 2 
#Program that inputs grammar text files and outputs the various outputs up to a certain length
 
import sys
import string
from collections import defaultdict

max_len = 3
file = "Binary.txt"
argv_len = len(sys.argv)

if argv_len == 2:
	file = sys.argv[1]
if argv_len == 3:
	if sys.argv[1][0] == "-" and sys.argv[1][1] == "l":
		max_len = int(sys.argv[1][2:])
		file = sys.argv[2]
		
dict = defaultdict(str)
worklist = []

for line in open(file, "r"):
	list = line.split()
	equal_sign_index = list.index("=")
	if list[equal_sign_index - 1] not in dict: #If NT on left side of equal sign is not already in the dictionary
		if len(list) - 2 == 2: #If list has 2 items on right side of equal sign
			items_str = list[2] + " " + list[3]
			items_list = []
			items_list.append(items_str) #Create list to keep track of values
			dict[list[equal_sign_index - 1]] = items_list #changed from list to str
		else: #If list has only 1 item on right side of equal sign
			items_str = list[2]
			items_list = []
			items_list.append(items_str)
			dict[list[equal_sign_index - 1]] = items_list
			
	elif list[equal_sign_index - 1] in dict: #If NT on left side of equal sign is an existing dictinoary key
		if len(list) - 2 == 1: #If list has only 1 item on the right side of equal sign
			items_str = list[2]
			dict[list[equal_sign_index - 1]].append(items_str) #Append string to existing list
	print(line)

 #Save first NT in file when reading
x = 2
for key in dict: #Separate for loop, ends before while loop
	worklist.append(key)
	while x == 2: #worklist: #If worklist is empty
		for i in range(0, len(dict.values()) - 1):
			temp = dict[worklist[0]][i] #temp assigned to first(current) value of worklist
			worklist.append(temp)
			print(temp)
		worklist.remove(worklist[0]) #Effectively "replaces" dictionary key with its values by removing first value in the worklist
		
		x -= 1
		

print(worklist)
print(dict)		
	
