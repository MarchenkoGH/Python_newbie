spisok = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(spisok)
x = abs(float(input("Введите число х: ")))
if x in spisok:
    print("abs(x) в списке присутствует",x)
else:
    print("Числа в списке нет")
