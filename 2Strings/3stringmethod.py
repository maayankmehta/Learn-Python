#string methods

#len() finds length of string
print(len(find_second_letter1))
#output: 11

#lower() converts to lower case
print(find_second_letter1.lower())
#output: hello hello

#upper() converst to caps
print(find_second_letter1.upper())
#output: HELLO HELLO

#str() converts non string to string
age = 22
print(str(age))
#output: 22

#isalpha() checks is the string contains only alphabets or not
choice = "select any one"
print(choice.isalpha())
#output: True

choice1 = "select any 1"
print(choice1.isalpha())
#output: False