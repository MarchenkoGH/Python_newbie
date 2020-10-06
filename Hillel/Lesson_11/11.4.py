def fake_string(original_string, old_word, new_word, changes):
    return original_string.replace(old_word, new_word, changes)


print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1))
