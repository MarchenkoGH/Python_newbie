def check_palindrome(any_word):
    a_z = any_word
    z_a = any_word[::-1]
    # print(a_z)
    # print(z_a)
    if a_z == z_a:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
    

check_palindrome(input('Please insert any word: \n'))
