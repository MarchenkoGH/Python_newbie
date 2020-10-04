temperature = int(input('Please input temperature: '))
temperature_unit = (input('Please input temperature unit, C for Celcius, K for Kelvin, F for Fahrenheit: ')).lower()


if temperature_unit == 'c':
    temperature_c = temperature
    temperature_k = temperature_c + 273.15
    temperature_f = temperature_c * 1.8 + 32
elif temperature_unit == 'k':
    temperature_k = temperature
    temperature_c = temperature_k - 273.15
    temperature_f = temperature_k * 1.8 - 459.67
elif temperature_unit == 'f':
    temperature_f = temperature
    temperature_k = (temperature_f + 459.67) / 1.8
    temperature_c = (temperature_f - 32) / 1.8
else:
    print('Please insert temperature unit correctly')


print(f'''Temperature in Celcius = {temperature_c}
Temperature in Kelvin = {temperature_k}\nTemperature in Fahrenheit = {temperature_f}''')
