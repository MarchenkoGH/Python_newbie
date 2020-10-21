import argparse
import csv


def check_optional_args(args):
    if (args.brand and args.color and args.year and args.fuel and args.reg_num) is None:
        raise SystemExit('There are no optional arguments, program will be terminated')
    return read_from_csv(args)


def read_from_csv(args):
    clean_args_dict = {k: v for k, v in vars(args).items() if v}
    # print(clean_args_dict)
    with open('o.csv', encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:

    return


def write_to_file():
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Cars' registration log book")
    parser.add_argument('o', help='File data in CSV format')
    parser.add_argument('--brand', help='Brand')
    parser.add_argument('--color', help='Color')
    parser.add_argument('--year', help='Year')
    parser.add_argument('--fuel', help='Fuel')
    parser.add_argument('--reg_num', help='Registry number')
    args = parser.parse_args()
    check_optional_args(args)
    print(vars(args))
    # print(args.brand)
