# for Reading File
filename = 'vikash.txt' 
with open(filename) as file_object:     
	lines = file_object.readlines() 

for line in lines:     
	print(line) 
	
# for writing
filename = 'vikash.txt' 
with open(filename, 'w') as file_object:     
	file_object.write("I love programming.") 
	
#append to a file
filename = 'vikash.txt' 
with open(filename, 'a') as file_object:     
	file_object.write("\nI love making games.")