import re
import csv


def car_number(string):
    full_match = re.fullmatch(r'(?:[A-ZА-Я]{2}\d{4}[A-ZА-Я]{2})', string, flags=re.ASCII)
    if full_match is None:
        print("The string you have entered isn't an Ukrainian car number")
    else:
        region_code = (re.match(r'(?:[A-ZА-Я]{2})', string)).group(0)
        print(region_code)
        return get_region(region_code)


def get_region(region_code):
    with open('ua_auto.csv', 'r') as file:
        dict_2004 = {line[1]: line[0] for line in csv.reader(file)}
        # print(dict_2004)
        print(dict_2004.get(region_code))
        # dict_2013 = {line[2]: line[0] for line in csv.reader(file)}

        # print(dict_2013)


car_number(input('Please insert your car number: '))
