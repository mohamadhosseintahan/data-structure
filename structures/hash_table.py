class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size


    def __hash(self, key):
        my_hash = 0

        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash
    

    def print_value(self):
        for i, val in enumerate(self.data_map):
            print(f"{i} : {val}")

    def set_item(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] is None:
            self.data_map[index] = []

        self.data_map[index].append([key, value])

    def get_item(self,key):
        index = self.__hash(key)

        if self.data_map[index] is not  None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
                
        return None
        

    def keys(self):
        all_keys = []

        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])

        return all_keys
        

ht = HashTable()

ht.set_item("mamad", 2)
ht.set_item("reza", 7)
ht.set_item("ali", 3)
ht.set_item("asqar", 6)
ht.set_item("jafar", 1)
ht.set_item("hadi", 5)
ht.set_item("akbar", 4)

print(ht.get_item("akbar"))
print(ht.get_item("hamid"))


print(ht.keys())
ht.print_value()