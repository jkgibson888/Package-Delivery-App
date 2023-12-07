#initializor for a package object
class Package:
    def __init__(self, id_num, address, city, zip, deadline, weight, note):
        self.id_num = id_num
        self.address = address
        self.city = city
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.status = 'At Hub'
        self.delivery_distance = 0
        self.delivery_time = ""
        self.departure_time = None

    #function to change final delivery parameters of a package
    def change_delivered(self, package, distance, time):
        package.delivery_distance = distance
        package.delivery_time = time

    #function to update the status of a package
    def update_status(self, package, string):
        package.status = string

    def __str__(self):
        return f'{self.id_num} {self.address} {self.city} {self.zip} {self.deadline} {self.delivery_time} {self.weight} {self.status} {self.delivery_distance}'

    def status_for_time(self, user_time):
        #check if truck has departed
        if self.departure_time > user_time:
            status = "At Hub"
        #check if still en route
        elif self.delivery_time > user_time:
            status = "En Route"
        #otherwise has been delivered
        else:
            status = "Delivered"

        return f'{self.id_num} {self.address} {self.city} {self.zip} {self.deadline} {self.delivery_time} {self.weight} {status} {self.delivery_distance}'
