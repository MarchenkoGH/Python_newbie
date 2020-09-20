def area_of_figure(a: int, b: int, figure = 'треугольник'):
    area = 0
    if figure == 'треугольник':
        print('вы выбрали треугольник')
        area = a * b * .5
        return area
    elif figure == 'треугольник':
        print('вы выбрали прямоугольник')
        area = a * b
        return area
    else:
        return 'ERROR. Вы должны правильно написать фигуру'



figure = (input('Выберете фигуру и введите нужное имя (треугольник или прямоугольник): '))
a = int(input('Введите длину стороны 1: '))
b = int(input('Введите длину стороны 2: '))


print('его площадь равна =', area_of_figure(a, b, figure))
