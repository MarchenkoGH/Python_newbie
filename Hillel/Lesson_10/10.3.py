def shift():
    return print(list[(steps * -1):] + list[:(steps * -1)])


list = [1, 2, 3, 4, 5]
steps = -2
shift()
