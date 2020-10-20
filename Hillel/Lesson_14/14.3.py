import re


def password_check():
    while True:
        password = input('Please insert your password: ')  # 'asDF65+5'
        if re.search(r'[a-z]', password) is None:
            print('In your password should be at least 1 symbol a-z')
        elif re.search(r'[A-Z]', password) is None:
            print('In your password should be at least 1 symbol A-Z')
        elif re.search(r'[0-9]', password) is None:
            print('In your password should be at least 1 symbol 0-9')
        elif re.search(r'[-#+@$=]', password) is None:
            print('In your password should be at least 1 symbol $#@-+=')
        elif len(password) < 8:
            print('In your password should have at least 8 symbols')
        elif re.fullmatch(r'(?:[a-zA-Z0-9$#@+-=]{8,})', password, flags=re.ASCII):
            print('Password is correct')
            break


password_check()
