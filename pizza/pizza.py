import sys
import csv
from tabulate import tabulate

def main():
    arguments = sys.argv
    check_status = check_argument(arguments)
    formatted_table = format_csv(check_status, arguments)
    print(formatted_table)

def check_argument(arguments):
    arguments_size = len(arguments)
    if arguments_size < 2:
        sys.exit("Too few command-line arguments")
    elif arguments_size > 2:
        sys.exit("Too many command-line arguments")
    else:
        if arguments[1].endswith(".csv"):
            return True
        else:
            sys.exit("Not a csv file")

def format_csv(check_status, arguments):
    if check_status:
        try:
            with open(arguments[1]) as file:
                reader = csv.DictReader(file)
                return tabulate(reader, headers="keys", tablefmt="grid")
        except FileNotFoundError:
            sys.exit("File not exist")

if __name__ == "__main__":
    main()
