# Lesson 3.1

a, b, c = int(input()) # первый вариант решения задачи
print(a + b + c)

print(sum([int(x) for x in input()])) # второй вариант решения задачи


# Lesson 3.2
x = float(input('введите число в формате ##.##: '))
y = x - x // 1
y = "{:.2f}".format(y)
print(y)

# Lesson 3.3
list_ten = [10, 20, 30, 40, 50]
print(list_ten.reverse()) # не хочет печатать list_ten
print(list_ten[::-1])

# Lesson 3.4
list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
for number in list_of_six:
    if number % 5 == 0:
        print(number)
    if number > 150:
        break

# Lesson 3.5 - НЕ РАБОТАЕТ ЦИКЛ
# import random
# x2 = random.randint(1, 10)
# i = 3:
# for i < 3:
#     x1 = int(input('введите число от 1 до 10: '))
#         print('ты ввел:', x1)
#     i -= 1
# else:
# print('You won!') if x1 == x2 else print('You lose!')


# Lesson 3.6

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x2 - x1 == 2 and y2 - y1 == 1:
    print('yes')
else:
    print('no')

# Lesson 3.7

x = int(input())
factorial = 1
while x > 0:
    factorial *= x
    x -= 1
print(factorial)
