def dict_without_empty_values(my_dict):
    new_dict = {key: values for key, values in my_dict.items() if values != None}
    return new_dict


my_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
print(dict_without_empty_values(my_dict))
