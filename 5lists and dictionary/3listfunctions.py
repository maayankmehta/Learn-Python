#list functions

#append : app items to the list

new_list = ['item1','item2','item3']
print(new_list)
#output: ['item1', 'item2', 'item3']

new_list.append('item4')
new_list.append('item5')
new_list.append('item6')
print(new_list)
#output: ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']


#find length of the list/ number of items in the list

print(len(new_list))
#output: 6

#inserting at specific index
new_list.insert(2,"inserted item")
print(new_list)
#output: ['item1', 'item2', 'inserted item', 'item3', 'item4', 'item5', 'item6']

#finding the index of a specific item

print(new_list.index("inserted item"))
#output: 2

#sorting the list
num = [5,3,6,2,8,1,7]
num.sort()
print(num)
#output: [1, 2, 3, 5, 6, 7, 8]

#remove item
num.remove(6)
print(num)
#output: [1, 2, 3, 5, 7, 8]

#alternate methods to remove list element
num.pop(5)
del(num(4))
