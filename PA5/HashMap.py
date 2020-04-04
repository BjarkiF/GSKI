from Bucket import Bucket
from Exceptions import ItemExistsException
from Exceptions import NotFoundException

class HashMap:
    def __init__(self):
        self.array_length = 4
        self.hash_table = [Bucket() for _ in range(self.array_length)]
        self.items_count = 0

    def insert(self, key, data):
        bucket = self.hash_table[hash(key) % self.array_length]
        try:
            bucket.find(key)
            raise ItemExistsException
        except NotFoundException:
            bucket[key] = data
            self.items_count += 1
            if self.items_count >= self.array_length * 1.2:
                self._rebuild()

    def update(self, key, data):
        bucket = self.hash_table[hash(key) % self.array_length]
        try:
            bucket.find(key)
            bucket[key] = data
        except NotFoundException:
            return NotFoundException

    def find(self, key):
        bucket = self.hash_table[hash(key) % self.array_length]
        try:
            data = bucket[key]
            return data
        except NotFoundException:
            raise NotFoundException

    def contains(self, key):
        try:
            self.find(key)
            return True
        except NotFoundException:
            return False

    def remove(self, key):
        bucket = self.hash_table[hash(key) % self.array_length]
        try:
            bucket.remove(key)
            self.items_count -= 1
        except NotFoundException:
            raise NotFoundException

    def __setitem__(self, key, data):
        bucket = self.hash_table[hash(key) % self.array_length]
        try:
            bucket.update(key, data)
        except NotFoundException:
            bucket.insert(key, data)
            self.items_count += 1
            if self.items_count >= self.array_length * 1.2:
                self._rebuild()

    def __getitem__(self, key):
        bucket = self.hash_table[hash(key) % self.array_length]
        return bucket.find(key)

    def __len__(self):
        return self.items_count

    def _rebuild(self):
        temp_data_pairs = []
        for bucket in self.hash_table:
            node = bucket.head
            while node is not None:
                temp_data_pairs.append([node.key, node.data])
                node = node.next
        self.array_length += self.array_length
        self.hash_table = [Bucket() for _ in range(self.array_length)]
        for item in temp_data_pairs:
            self.insert(item[0], item[1])

if __name__ == "__main__":
    map = HashMap()
    map.insert(1, "data 1")
    map.insert(2, "data 2")
    map.insert(3, "data 3")
    map.insert(4, "data 4")
    map.insert(5, "data 5")