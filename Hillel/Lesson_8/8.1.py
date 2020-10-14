import datetime
import requests
import json
from pprint import pprint


def currency_exchange(start_date, currency_from, currency_to, amount):
    result = [['date', 'from', 'to', 'amount', 'rate', 'result']]
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
    return pprint(result)


def values_validation(args):
    if isinstance(args.amount, float):
        amount = args.amount
    else:
        amount = 100.00  # using 100.00 by default

    if datetime.datetime.strptime(args.start_date, "%Y-%m-%d") > datetime.datetime.now():
        start_date = datetime.datetime.now()
    else:
        start_date = datetime.datetime.strptime(args.start_date, "%Y-%m-%d")

    with open('symbols.json') as file:
        currency_codes = json.load(file)
        currency_list = [symbols for symbols in currency_codes['symbols']]
        currency_from = args.currency_from.upper()
        if currency_from not in currency_list:
            # print('The currency code you have entered is wrong, will use "USD" by default')
            currency_from = 'USD'  # using 'USD' by default
        currency_to = args.currency_to.upper()
        if currency_to not in currency_list:
            # print('The currency code you have entered is wrong, will use "UAH" by default')
            currency_to = 'UAH'  # using 'UAH' by default
    return currency_exchange(start_date, currency_from, currency_to, amount)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='currency exchange')
    parser.add_argument('currency_from', type=str, default='USD',
                        help='currency code you want to convert from, default = USD')
    parser.add_argument('currency_to', type=str, default='UAH',
                        help='currency code you want to convert to, default = UAH')
    parser.add_argument('--start_date', type=str, default=datetime.datetime.now(),
                        help='the date from we start to look for exchange, default = today')
    parser.add_argument('amount', type=float, default=100.00,
                        help='the amount we need to change, default = 100.00')
    args = parser.parse_args()
    values_validation(args)
