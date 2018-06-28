#dictionaries : list with key and value instead of index

#declaring a dictionary
dictionary = {'key1' : 1, 'key2' : 2, 'key3' : 3, 'key4' : ['l1','l4','l3','l2']}

#access value using key
print(dictionary['key2'])
#output: 2

#new entry to dictionary
#dict_name[new_key] = new_value
dictionary['key5'] = 5

#dictionary functions
#dict_name['list_key'].method()

dictionary['key4'].sort()
print(dictionary['key4'])
#output: ['l1', 'l2', 'l3', 'l4']

dictionary['key4'].remove('l4')
print(dictionary['key4'])
#output: ['l1', 'l2', 'l3']
