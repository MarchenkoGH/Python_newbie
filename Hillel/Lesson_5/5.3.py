def area_of_figure():
    figure = int(input('Введите количество сторон фигуры (напр. 3 для треугольника и 4 для прямоугольника): '))
    storona_1 = int(input('Введите длину стороны 1: '))
    storona_2 = int(input('Введите длину стороны 2: '))
    area = 0
    if figure == 3:
        print('вы выбрали треугольник')
        area = storona_1 * storona_2 * .5
    elif figure == 4:
        print('вы выбрали прямоугольник')
        area = storona_1 * storona_2
    else:
        print('ERROR. Вы должны ввести число 3 или 4')
    return area

print('площадь фигуры равна =', area_of_figure())
