my_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
new_dict = {key: values for key, values in my_dict.items() if values != None}
print(new_dict)
