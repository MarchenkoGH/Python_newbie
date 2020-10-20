import re


password = input('Please insert your password: ')  # 'asDF65+5'
pattern = r'(?:[a-zA-Z0-9$#@+-=]{8,})'
full_match = re.fullmatch(pattern, password, flags=re.ASCII)
while full_match is None:
    print('Please insert your password again')
    print('Your password is correct')
    
