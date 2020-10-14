import datetime
import requests
import json


def currency_exchange(currency_from, currency_to, start_date, amount):
    # currency_from = str(input('Please insert currency code you want to convert from: '))
    # currency_to = str(input('Please insert currency code you want to convert to: '))
    # start_date = str(input('Please insert date of exchange in format yyyy-mm-dd: '))
    # amount = float(input('Please insert amount you want to change: '))
    result = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    while start_date <= datetime.datetime.now():
        url = requests.get('https://api.exchangerate.host/convert',
                           params={'from': currency_from, 'to': currency_to,
                                   'amount': amount, 'date': start_date})
        data = url.json()
        result.append([data['date'],
                       data['query']['from'],
                       data['query']['to'],
                       data['query']['amount'],
                       data['info']['rate'],
                       data['result']])
        start_date += datetime.timedelta(days=1)
    print(result)


currency_exchange('USD', 'UAH', '2020-10-10', 100.00)
