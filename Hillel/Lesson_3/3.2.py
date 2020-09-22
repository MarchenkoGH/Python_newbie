# x = float(input('введите число в формате ##.##: '))
# y = x - x // 1
# y = "{:.2f}".format(y)
# print(y)
 
# замечание принял, исправил решение т.к. не правильно понял задание

x = float(input('Please input number in following format ##.##: '))
fractional_part = int(x * 100 % 100)
second_number = int(x * 10 % 10)
print(fractional_part, second_number, sep="\n")
