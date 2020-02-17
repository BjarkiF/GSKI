class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        ret_string = ''
        node = self.head
        while node is not None:
            ret_string += str(node.data) + ' '
            node = node.next
        return ret_string

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node

    def pop_front(self):
        if self.head is None:
            return None
        else:
            value = self.head.data
            self.head = self.head.next
            return value

    def get_size(self):
        counter = 0
        node = self.head
        while node is not None:
            counter += 1
            node = node.next
        return counter
