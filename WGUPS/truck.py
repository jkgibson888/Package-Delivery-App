from package import*

#initializor for a truck object
class Truck:
    def __init__(self, truck_id, package_list, starting_time):
        self.truck_id = truck_id
        self.package_list = package_list
        self.starting_time = starting_time
        self.max_package = 16
        self.average_speed = 18
        self.current_packages = 0

        self.list = []

    #function to add a package to a trucks associated package package list
    def add_package(self, package):
        self.list.append(package)