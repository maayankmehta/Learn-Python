
#function calling function

def first_function(parameter_1):
	print("this is the argument passed to function 2: " +str(parameter_1))

def second_function(parameter_2):
	return first_function(parameter_2) #calls the first function

second_function("paper") #calls the second function
