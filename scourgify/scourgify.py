import sys
import csv

def main():
    arguments = sys.argv
    if not check_arguments(arguments):
        sys.exit()

    try:
        with open(arguments[1], newline='') as infile:
            reader = csv.DictReader(infile)
            data = []
            for row in reader:
                names_row = row["name"]
                house_row = row["house"]

                last, first = map(str.strip, names_row.split(", "))
                data.append({"first": first, "last": last, "house": house_row})

        with open(arguments[2], "w", newline='') as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {arguments[1]}")

def check_arguments(arguments):
    # Check for the correct number of arguments
    if len(arguments) != 3:
        if len(arguments) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")
    # Check that both input and output files have .csv extensions
    if not arguments[1].endswith(".csv") or not arguments[2].endswith(".csv"):
        print("Invalid file format. Only CSV files are allowed.")
        return False
    return True

if __name__ == "__main__":
    main()
