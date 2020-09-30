my_list = ['a', 'b', 'c', 'd', 'e']
list_of_indexes = [i for i in range(len(my_list))]
new_dict = {keys: values for keys, values in zip(list_of_indexes, my_list)}
print(new_dict)
