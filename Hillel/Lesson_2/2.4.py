distance = float(input("Введите расстояние трассы (км): "))
start = float(input("Укажите отметку с которой стартует Вася: "))
v = float(input("Пожалуйста введите скорость (км/ч): "))
t = float(input("пожалуйста введите время (ч): "))
if v > 0:
    stop = start + v * t
    print("До финиша осталось: ", distance - stop, "км")
elif v < 0:
    stop = start - abs(v * t)
    print("Вася едет не в ту сторону, до финиша осталось: ", distance - stop, "км")
else:
    print("Вася, ты уже стоишь", t,"ч")
