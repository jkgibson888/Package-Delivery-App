class HashTable:
    #initializor for the hash table object
    def __init__(self, initial_capacity = 10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    #function to insert a package into the hash table
    def insert(self, key, package):
        bucket = hash(package.id_num) % len(self.table)
        bucket_list = self.table[bucket]

        key_value = [key, package]

        #if key is present in list update associated package
        for value in bucket_list:
            if value[0] == key:
                value[1] = package
                return True

        #if not, insert package to end of bucket list
        bucket_list.append(key_value)
        return True

    #search for a package in the hash table
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #if key is found in bucket list return associated package
        for value in bucket_list:
            if(value[0] == key):
                return value[1]

        #no key value found in bucket list so return nothing
        else:
            return None

    #remove a package from the hash table
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        #if key found in bucket list remove the key and associated package
        if key in bucket_list:
            bucket_list.remove(key)
