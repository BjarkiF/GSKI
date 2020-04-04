from Exceptions import ItemExistsException
from Exceptions import NotFoundException

class BucketNode:
    def __init__(self, key = None, data = None, next = None):
        self.key = key
        self.data = data
        self.next = next

class Bucket:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key, data):
        new_node = BucketNode(key, data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        try:
            self.find(key)
            raise ItemExistsException
        except NotFoundException:
            self.tail.next = new_node
            self.tail = new_node
            return

    def update(self, key, data):
        found = False
        node = self.head
        while node is not None:
            if node.key == key:
                found = True
                node.data = data
                break
            node = node.next
        if not found:
            raise NotFoundException

    def find(self, key):
        found = False
        found_data = 0
        node = self.head
        while node is not None:
            if node.key == key:
                found = True
                found_data = node.data
                break
            node = node.next
        if found:
            return found_data
        else:
            raise NotFoundException

    def contains(self, key):
        try:
            self.find(key)
            return True
        except NotFoundException:
            return False

    def remove(self, key):
        node = self.head
        found = False
        if node.key == key:
            self.head = node.next
        while node.next is not None:
            if node.next.key == key:
                found = True
                if node.next == self.tail:
                    self.tail = node
                    break
                else:
                    node.next = node.next.next
                    break
            node = node.next
        if not found:
            raise NotFoundException

    def __setitem__(self, key, data):
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        count = 0
        node = self.head
        if node is None:
            return count
        while node is not None:
            count += 1
            node = node.next
        return count

if __name__ == "__main__":
    b = Bucket()
    b.insert(3, "data")
    b.insert(5, "abc")
    b.insert(1, "lmao")
    b.remove(5)
    print(b.find(5))