import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"], restval="happy land")
    writer.writerow({"name": name, "home": home})











