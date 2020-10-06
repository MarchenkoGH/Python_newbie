def longest_word(some_test):
    words = some_test.split()
    length = []
    for i in range(len(words)):
        length.append(len(words[i]))
        i += 1
    dictionary = dict(zip(length, words))
    print(dictionary)
    return dictionary[max(length)]

print(longest_word("What makes a good man"))
