names = []

# Open the names.txt file in read mode
with open("names.txt", "r") as file:
    # Read each line, remove trailing whitespace, and add to the names list
    for line in file:
        names.append(line.rstrip())

# Sort the names and print a greeting for each
for name in sorted(names):
    print(f"hello, {name}")