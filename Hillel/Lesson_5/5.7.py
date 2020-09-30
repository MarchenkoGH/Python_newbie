import datetime


def is_date():
    try:
        date = datetime.date(year, month, day)
        return True
    except ValueError:
        print('You have inserted wrong parameters, please try again')
        return False


day = int(input('Please insert day: '))
month = int(input('Please insert month: '))
year = int(input('Please insert year: '))
print(is_date())
