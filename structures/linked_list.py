class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_val = None

class LinkedList:
    length = 0
    def __init__(self):
        # head val should be a Node instance
        self.head_val = None

    def print_data(self):
        print_value = self.head_val
        while print_value is not None:
            print(print_value.data_val)
            print_value = print_value.next_val

    def add_begining(self, data):
        new_node = Node(data)
        new_node.next_val = self.head_val
        self.head_val = new_node

        self.length += 1

    def add_end(self, data):
        new_node = Node(data)
        if self.head_val is None:
            self.head_val = new_node
            self.length += 1
            return 
        last_node = self.head_val
        while last_node.next_val:
            last_node = last_node.next_val

        last_node.next_val = new_node
        self.length += 1

    def add_middle(self, point_node, data):
        if not point_node:
            print("point node is absent")
            return
        new_node = Node(data)
        new_node.next_val = point_node.next_val
        point_node.next_val = new_node

        self.length += 1

    def pop_first(self):
        if self.head_val is None:
            return

        if self.head_val.next_val:
            self.head_val = self.head_val.next_val
        else:
            self.head_val = None

        self.length -= 1

    def pop(self):
        if self.head_val is None:
            return
        
        if self.head_val.next_val is None:
            self.head_val = None
            self.length -= 1
            return
        
        temp = self.head_val
        last_item = None 
        while temp.next_val:
            last_item = temp
            temp = temp.next_val

        last_item.next_val = None
        self.length -= 1

    def get(self, index):
        if index < 0 or index > self.length:
            return
        
        temp = self.head_val

        for _ in range(index):
            temp = temp.next_val

        return temp
    
    def set(self, index, value):
        temp = self.get(index)

        if temp:
            temp.data_val = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return

        elif self.length == index:
            self.add_end(value)
            return
        elif index == 0:
            self.add_begining(value)
            return

        temp = self.get(index - 1)
        new_node = Node(value)
        new_node.next_val = temp.next_val
        temp.next_val = new_node
        self.length += 1
        
    def remove(self, index):
        if index < 0 or index > self.length:
            return

        elif index == self.length:
            self.pop()
            return
        elif index == 0:
            self.pop_first()
            return
        
        previos_node = self.get(index - 1)
        next_node = self.get(index + 1)
        previos_node.next_val = next_node
        self.length -= 1

    def reverse(self):
        temp = self.head_val
        before = None

        for _ in range(self.length):
            after = temp.next_val
            temp.next_val = before
            before, temp = temp, after

        self.head_val = before
        
        
linked_list = LinkedList()

linked_list.add_end("Mon")

linked_list.add_end("Tue")

linked_list.add_end("Wed")

linked_list.add_end("Thu")

linked_list.add_end("Sat")

linked_list.add_begining("Sun")

linked_list.add_middle(linked_list.head_val.next_val.next_val.next_val.next_val, "Fri")

linked_list.pop_first()

linked_list.pop()

linked_list.insert(3, "test for insert")

linked_list.remove(3)

linked_list.reverse()

linked_list.print_data()