def area_of_figure(a: int, b: int, figure = 'triangle'):
    area = 0
    if figure == 'triangle':
        print('your choice is triangle')
        area = a * b * .5
        return area
    elif figure == 'rectangle':
        print('Your choice is rectangle')
        area = a * b
        return area
    else:
        return 'ERROR. You have to chooce between triangle and rectangle'



figure = (input('Please choice between triangle and rectangle and input the name accordinly): '))
a = int(input('Please enter length of side 1: '))
b = int(input('Please enter length of side 2: '))


print('The area is = ', area_of_figure(a, b, figure))
