import sys

def main():
    arguments = sys.argv
    check_status = check_arguments(arguments)
    number_of_lines = count_lines(check_status, arguments)
    print(number_of_lines)

def check_arguments(arguments):
    arguments_size = len(arguments)
    if arguments_size < 2:
        sys.exit("Too few command-line arguments")
    elif arguments_size > 2:
        sys.exit("Too many command-line arguments")
    else:
        if arguments[1].endswith(".py"):
            return True
        else:
            sys.exit("Not a Python file")

def count_lines(check_status, arguments):
    try:
        if check_status:
            with open(arguments[1], "r") as file:
                line_number = 0
                for line in file:
                    line = line.lstrip()
                    if line.startswith("#") or line == "":
                        continue
                    else:
                        line_number += 1
                return line_number
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()

