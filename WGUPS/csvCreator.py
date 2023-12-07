import csv
from hashTable import*
from package import*

#read package data from csv file and then initialize each package object and insert it into the hash table
def createPackages(hash_table):
    with open('files\packages.csv') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=',')
        for row in file_reader:
            new_package = Package(int(row[0]), row[1], row[2], row[4], row[5], row[6], row[7])
            hash_table.insert(new_package.id_num, new_package)

#read the distance table and bring the distances into the program
def createDistances(distance_table):
    with open('files\distance_table.csv') as csv_file:
        file_reader = csv.reader(csv_file, delimiter=',')
        for row in file_reader:
            distance_table.append(row)
