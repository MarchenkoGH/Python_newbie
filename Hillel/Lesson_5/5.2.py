some_text = input('Please enter any text: ')
print(f'Number of characters in this text: {len(some_text)} \nNumber of words in this text: {len(some_text.split())}')

# second code
letters = 0
spaces = 0
some_text = input('Please enter any text: ')
symbols_in_test = len(some_text)
for i in range(len(some_text)):
    if some_text[i] == " ":
        spaces += 1
    else:
        letters += 1
print(f'Number of symbols in this text: {symbols_in_test} \nNumber of words in this text : {spaces + 1}')
print(f'Number of characters in this text : {letters} \nNumber of spases in this text: {spaces}')
