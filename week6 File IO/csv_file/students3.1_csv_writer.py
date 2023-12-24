import csv

name = input("What's your name? ")
home = input("Where's your home? ")


with open("students3.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])








# import csv
# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



# # Spam Spam Spam Spam Spam |Baked Beans|
# # Spam |Lovely Spam| |Wonderful Spam|
