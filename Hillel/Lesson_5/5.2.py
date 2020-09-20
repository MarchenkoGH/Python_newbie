some_text = input('Введите какой то текст: ')
print(f'Количество символов в тексте: {len(some_text)} \nКоличество слов в тексте: {len(some_text.split())}')

# second code
letters = 0
spaces = 0
some_text = input('Введите какой то текст: ')
symbols_in_test = len(some_text)
for i in range(len(some_text)):
    if some_text[i] == " ":
        spaces += 1
    else:
        letters += 1
print(f'Количество символов в тексте: {symbols_in_test} \nКоличество слов в тексте : {spaces + 1}')
print(f'Количество букв в тексте : {letters} \nКоличество пробелов в тексте: {spaces}')
