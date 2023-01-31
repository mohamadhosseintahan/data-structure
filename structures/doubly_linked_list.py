class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        
        if index < self.length / 2: 
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp
    
    def set(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value

            return True

        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)

        before = self.get(index -1)
        after = before.next

        new_node.next = after
        new_node.prev = before

        after.prev = before.next = new_node

        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        
        temp = self.get(index)

        after = temp.next
        before = temp.prev

        after.prev = before
        before.next = after

        temp.prev = temp.next = None

        self.length -= 1
        return temp

linked_list = DoublyLinkedList()

linked_list.append("0")

linked_list.append("1")

linked_list.append("2")

linked_list.append("3")

linked_list.append("4")

linked_list.append("5")

linked_list.append("6")

linked_list.append("7")

linked_list.append("8")

linked_list.pop()

linked_list.prepend("-1")

linked_list.pop_first()

linked_list.print()