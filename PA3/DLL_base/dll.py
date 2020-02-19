
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self._head = None
        self._tail = None
        self._curr = None

    def __str__(self):
        node = self._head
        ret_str = ''
        while node is not None:
            ret_str += str(node.data) + ' '
            node = node.next
        return ret_str[:-1]

    def __len__(self):
        node = self._head
        len_counter = 0
        if node is None:
            return len_counter
        else:
            while node is not None:
                len_counter += 1
                node = node.next
        return len_counter

    def insert(self, value):
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            if self._curr.prev is not None:
                self._curr.prev.next = new_node
                new_node.prev = self._curr.prev
            else:
                self._head = new_node
            self._curr.prev = new_node
            new_node.next = self._curr
        self._curr = new_node

 # TODO: myndast loop hér - curr.next bendir alltaf á sjálft sig og fer í hring
    def remove(self):
        if self._curr is None:
            return
        else:
            if self._curr.next is None and self._curr.prev is None:
                self._head = None
                self._tail = None
                self._curr = None
                return
            elif self._curr.next is  None:
                self._curr.prev.next = None
                self._curr.prev = self._tail
                self._curr = self._curr.prev
                return
            elif self._curr.prev is None:
                self._curr.next.prev = None
                self._curr.next = self._head
            else:
                self._curr.prev.next = self._curr.next
                self._curr.next.prev = self._curr.prev
        self._curr = self._curr.next
        return

    def get_value(self):
        if self._curr is None:
            return None
        else:
            return self._curr.data

    def move_to_next(self):
        if self._curr.next is None:
            return
        else:
            self._curr = self._curr.next

    def move_to_prev(self):
        if self._curr.prev is None:
            return
        else:
            self._curr = self._curr.prev

    def move_to_pos(self, pos):
        if pos == 0:
            self._curr = self._head
            return
        pos_count = 0
        node = self._head
        while pos != pos_count:
            if node == self._tail:
                if pos_count < pos:
                    return
                break
            node = node.next
            pos_count += 1
        self._curr = node


dlist = DLL()
dlist.insert(1)
dlist.insert(2)
dlist.insert(3)
dlist.insert(4)
print(dlist)
dlist.remove()
dlist.move_to_prev()
dlist.move_to_prev()
dlist.move_to_next()
dlist.remove()
print(dlist)
dlist.move_to_pos(0)
dlist.insert(10)
dlist.insert(11)
dlist.insert(12)
dlist.move_to_pos(15)
dlist.insert(13)
dlist.insert(14)
print(dlist)
