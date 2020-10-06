def hide_email(email):
    first_part = email.split('@')[0][:-3]
    second_part = email.split('@')[1][3:]
    return first_part + '***' + '@' '***' + second_part


print(hide_email('shustriy1980@mail.ru'))
