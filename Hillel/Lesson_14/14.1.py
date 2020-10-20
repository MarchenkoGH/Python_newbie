import re
import csv


def car_number(string):
    full_match = re.fullmatch(r'(?:[A-ZА-Я]{2}\d{4}[A-ZА-Я]{2})', string, flags=re.ASCII)
    if full_match is None:
        print("The string you have entered isn't an Ukrainian car number")
    else:
        region_code = string[:2]
        # print(region_code)
        return get_region(region_code)


def get_region(region_code):
    with open('ua_auto.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if region_code in (row['Код 2004'], row['Код 2013'], row['Code 2004'], row['Code 2013']):
                return print(row['Регіон'])


car_number(input('Please insert your car number: ').upper())
