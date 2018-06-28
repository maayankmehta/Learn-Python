#list/string slicing

list_to_slice = ['a','b','c','d','e']

first_two_items = list_to_slice[0:2] #element at 0th position is included and from 3rd position are excluded
print(first_two_items)
#output: ['a', 'b']

first_two = list_to_slice[:2]
from_second_upto_last = list_to_slice[1:]
