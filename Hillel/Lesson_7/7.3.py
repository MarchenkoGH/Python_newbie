import requests
import datetime


def weather_request():
    api_key = 'f9ada9efec6a3934dad5f30068fdcbb8'
    city = input('Please insert name of city: ')
    cnt = int(input('Please insert qty of days: '))
    url = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?',
                       params={'q': city, 'cnt': cnt, 'units': 'metric', 'appid': api_key})
    data = url.json()
    file_name = datetime.datetime.now().strftime("%d-%m-%Y") + '-' + city + '-' + str(cnt) \
                + '-days-weather-forecast.txt'
    file = open(file_name, 'w')
    file.write('Date\t\t Day temperature\t Feels like\t Night temperature\n')
    for data_list in data['list']:
        file.write(str(datetime.datetime.fromtimestamp(data_list['dt']).strftime("%d-%m-%Y")) + '\t\t')
        file.write(str(data_list['temp']['day']) + '\t\t\t\t')
        file.write(str(data_list['feels_like']['day']) + '\t\t')
        file.write(str(data_list['temp']['night']) + '\t\n')
    file.close()


weather_request()
