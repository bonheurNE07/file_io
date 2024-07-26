import csv

# Prompt the user for their name and home
name = input("What's your name? ")
home = input("Where's your home? ")

# Open the students.csv file in append mode
with open("students.csv", "a") as file:
    # Create a CSV DictWriter object
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    # Write the user's input as a new row in the CSV file
    writer.writerow({"name": name, "home": home})
