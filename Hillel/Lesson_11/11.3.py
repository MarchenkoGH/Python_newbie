def longest_word(some_test):
    max_word = ''
    for word in some_test.split():
        if len(word) > len(max_word):
            max_word = word
    return max_word


print(longest_word("What makes a good man"))


# Second option
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
