#Joshua Gibson Student ID: 002204262
import csvCreator
import datetime
from datetime import timedelta
from hashTable import*
from truck import Truck

#The program loads package information into a hash table and loads distance information between various locations from another file.
#initialize hashtable and package list
hashed_packages = HashTable()
package_list = csvCreator.createPackages(hashed_packages)

#load the distance table into the program
distance_table = []
csvCreator.createDistances(distance_table)

#initialize a truck list for each truck
truck1_list = []
truck2_list = []
truck3_list = []

#Packages are “loaded” onto each truck within the program logic based on priority.
# load priority packages into truck 1 package list
truck1_list = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

#load delayed packages and truck 2 specific packages to truck 2 package list
truck2_list = [3, 6, 18, 25, 28, 32, 36, 38, 33, 35, 39]

#load EOD packages into truck 3 list
truck3_list = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27]


#create each truck
truck1 = Truck(1, truck1_list, "8:00 AM")
truck2 = Truck(2, truck2_list, "9:05 AM")
truck3 = Truck(3, truck3_list, "1:00 AM")

#cycle through each node between a starting index and a next index to find the shortest distance between the current package and the next package
def retrieve_distance(start, next):
    y = distance_table[0].index(next)
    x = distance_table[0].index(start)

    #if x is greater then y swap
    if x > y:
        temp = y
        y = x
        x = temp

    #retrieve distance from the distance table and return the distance
    distance = distance_table[y][x]
    return distance

#function to convert a string from user input to a time object
def convert_to_time(date_time):
    format = '%I:%M %p'
    datetime_string = datetime.datetime.strptime(date_time, format)
    return datetime_string

#Greedy algorithm
def greed_algorithm(truck):
    #initialize variables
    total = 0
    return_distance = 0
    start = "HUB"
    next = None
    smallest = 20.0
    new_start = None
    x = 0
    delivered_id = None

    #cycle through each package in the trucks package list
    while x < len(truck.package_list):

        for package_id in truck.package_list:
            package = hashed_packages.search(package_id)
            # if only one package left return to hub after delivery
            if len(truck.package_list) == 1:
                next = "HUB"
            else:
                next = package.address

            #find the distance between the last package and the next package
            distance = float(retrieve_distance(start, next))
            #if last package calculate distance back to hub
            if len(truck.package_list) == 1:
                smallest = float(retrieve_distance(start, next))
                delivered_id = package.id_num
            #else calculate distance to next package
            else:
                if package.address != start and distance < smallest:
                    delivered_id = package.id_num
                    new_start = next
                    smallest = distance
                    package_object_id = package.id_num

        total = total + smallest

        #update package
        update_package = hashed_packages.search(delivered_id)
        min = total/truck.average_speed * 60
        time = convert_to_time(truck.starting_time)
        delivered_time = time + timedelta(minutes=min)
        update_package.change_delivered(update_package, smallest, convert_to_time(delivered_time.strftime("%H:%M %p")))

        hashed_packages.insert(update_package.id_num, update_package)
        #print(hashed_packages.search(delivered_id).delivery_time)
        start = new_start

        #if one item left delete list
        if len(truck.package_list) == 1:
            del truck.package_list[-1]
        #otherwise delete the package object from the truck list
        else:
            truck.package_list.remove(package_object_id)
            smallest = 30

    return total

#Truck 1 and 2 are ran through the greedy algorithm
#put truck 1 and 2 through the greedy algorithm
distance = greed_algorithm(truck1)
greed_algorithm(truck2)

#fix package 9's address
package = hashed_packages.search(9)
package.address = "410 S State St"
package.zip = "84111"

#update truck 3 start time after truck one returns
new_time = convert_to_time(truck1.starting_time) + timedelta(minutes=distance/truck1.average_speed * 60)
truck3.starting_time = (new_time.strftime("%H:%M %p"))

#put truck 3 into the greedy algorithm
greed_algorithm(truck3)

#A function to simulate package delivery based on an input time
def deliver_packages(time):

    # load priority packages into truck 1 package list
    truck1_list = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

    # load delayed packages and truck 2 specific packages to truck 2 package list
    truck2_list = [3, 6, 18, 25, 28, 32, 36, 38, 33, 35, 39]

    # load EOD packages into truck 3 list
    truck3_list = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27]

    total_distance = 0
    # correct the status of packages on truck 1 based on user input
    for x in truck1_list:
        package = hashed_packages.search(x)
        package.departure_time = convert_to_time(truck1.starting_time)
        package.status_for_time(time)

    # correct the status of packages on truck 2 based on user input
    for x in truck2_list:
        package = hashed_packages.search(x)
        package.departure_time = convert_to_time(truck2.starting_time)
        package.status_for_time(time)

    # correct the status of packages on truck 3 based on users input
    for x in truck3_list:
        package = hashed_packages.search(x)
        package.departure_time = convert_to_time(truck3.starting_time)
        package.status_for_time(time)


print("----------------------------------------------------")


#starting distance travel

start = True
while start is True:

    print("Please choose an option:")
    print("1: Final details of packages")
    print("2:  Individual Package look up")
    print("3: Package list based on time")
    command_prompt = input("4: Exit    ")

    if command_prompt == "1":

        #print all packages with their completed status
        for i in range(1, 41):
            package = hashed_packages.search(i)
            print(package.status_for_time(convert_to_time("3:00 PM")))


        print("")
        print("-----------------------------------------------------------")
        print("")

    #print information for a specific package
    elif command_prompt == "2":

        #select package and time to view status
        user_response = int(input("Package ID:  "))
        package = hashed_packages.search(user_response)
        user_response = convert_to_time(input("Enter time with format HH:DD AM/PM   "))

        #print package
        print(package.status_for_time(user_response))
        print("")
        print("-----------------------------------------------------------")
        print("")

    #print package information for all packages based on user defined time
    elif command_prompt == "3":
        #user input
        user_response = convert_to_time(input("Enter time with format HH:DD AM/PM   "))

        distance = 0
        deliver_packages(user_response)

        #cycle through all the packages and update their status based on user input
        for i in range(1, 41):
            package = hashed_packages.search(i)
            print(package.status_for_time(user_response))
            #add up the distance for delivery
            if package.delivery_time < user_response:
                distance = distance + package.delivery_distance

        print("")
        print("Total distance traveled:  ", distance)
        print("")
        print("-----------------------------------------------------------")
        print("")

    elif command_prompt == "4":
        break






