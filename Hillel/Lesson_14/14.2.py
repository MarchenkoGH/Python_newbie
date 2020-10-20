import re


def phone_number_format(input_string):
    clean_number = re.sub(r'[^\d]', '', input_string)
    # print(clean_number)
    if len(clean_number) == 10:
        phone_number = re.sub(r'(\d{3})(\d{3})(\d\d)(\d\d)', r'(+38) \1 \2 \3-\4', clean_number)
        print(phone_number)
    elif len(clean_number) == 12:
        phone_number = re.sub(r'(\d\d)(\d{3})(\d{3})(\d\d)(\d\d)', r'(+\1) \2 \3 \4-\5', clean_number)
        print(phone_number)
    else:
        print('Failed to recognize number')
    return


phone_number_format('38063999hy-., 9999  ')
