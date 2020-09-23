# Lesson 3.5 - Теперь цикл работает верно
import random
x2 = random.randint(1, 10)
i = 0
while i < 3:
    x1 = int(input('please insert number in range 1 - 10: '))
    if x1 == x2:
        print(f'Computer inserted {x2}, You won!')
        break
    else:
        i += 1
        if i == 3:
            print(f'You have spent 3 attempts already, Computer inserted {x2}, bye!')
            break
        else:
            print('You you did not guess, try again!')
