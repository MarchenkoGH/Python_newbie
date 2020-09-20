import math


def square(a: int):
    area = a ** 2
    perimeter = a * 4
    diagonal = a * math.sqrt(2)
    kortezh = (area, perimeter, diagonal)
    return kortezh


a = int(input('Введите сторону квадрата: '))
print(square(a))
