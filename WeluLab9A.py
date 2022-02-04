#! /usr/bin/env python3


import csv

# Reading the csv file.
datafile = open('products.csv', 'r')
datareader = csv.reader(datafile, delimiter=',')

# Initializing an array to store the data read.
data = []

# Populating and checking the data array.
for line in datareader:
    data.append(line)
##print()
##print(data)
##print()

# Closing the file now that the data array has been populated.
datafile.close()

# Displaying the element arrays vertically.
##print()
##for element in data:
##    print(element, end="\n")
##print()

# Looping through the list to display the data.
print()
print("Original Data of the CSV File:")
print()
for row in data:
    for column in row:
        print(column, end=" | ")
    print()
print()


# Looping through the prices and raising them.
print()
print("Adding 10% to the price of all the products.")
print()
# This ensures I don't touch the labels
i = 1 
while i < len(data):
    price = float(data[i][3])
    price = price * 1.10
    # print(format(price, ",.2f")) # Pretty sure format makes it a str.
    data[i][3] = format(price, ",.2f")
    i += 1
for row in data:
    for column in row:
        print(column, end=" | ")
    print()
print()

# Simply adding another element to the csv file.
print()
print("Adding another element to the list of products.")
print()
data.append(['Food', 'Apples', '12', '3.75'])
for row in data:
    for column in row:
        print(column, end=" | ")
    print()
print()


# Creating a new .csv file with the manipulated data.
print()
print("***New CSV file updated_products.csv created!***")
print()
product_csv = open('updated_products.csv', "w", newline="")
cvsWriter = csv.writer(product_csv, delimiter=',')
cvsWriter.writerows(data)
product_csv.close()


# Using a simple if statement to check and print Hardware products.
print()
print("Printing the list of products for Hardware.")
print()
j = 1 
while j < len(data):
    p_cat = data[j][0]
    if p_cat.lower() == 'hardware':
        print(data[j][0] + " | " + data[j][1] + " | " + data[j][2] + " | " + data[j][3] + " | ")
    j += 1

print()
print()
    







