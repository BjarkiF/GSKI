from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self, type):
        if type == 'array':
            self._container = ArrayDeque()
        elif type == 'linked':
            self._container = LinkedList()

    def __str__(self):
        return self._container.__str__()

    def push(self, value):
        self._container.push_front(value)

    def pop(self):
        popped = self._container.pop_front()
        return popped

    def get_size(self):
        size = self._container.get_size()
        return size
