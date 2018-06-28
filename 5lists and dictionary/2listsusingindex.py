# index starts from 0

list_choices = ["rock","paper","scissors","replay"]
print(list_choices)
#output: ['rock', 'paper', 'scissors', 'replay']

print("your choice is " +str(list_choices[0])) #prints item at index 0
#output: your choice is rock

"""
select = input("select any 1 from 0 to 3 ")
print("your choice is '%s' " % str(choices[int(select)]))"""

#replacing list items using index
list_choices[0] = "pencil"
print(list_choices)
#output: ['pencil', 'paper', 'scissors', 'replay']
