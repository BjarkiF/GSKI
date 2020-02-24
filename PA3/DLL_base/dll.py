
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

    def _insert_tail(self, value):      # Notað í sort fallinu
        new_node = Node(value)
        new_node.prev = self._tail
        self._tail.next = new_node
        self._tail = new_node

    def _insert_head(self, value):      # Notað í sort fallinu
        new_node = Node(value)
        new_node.next = self._head
        self._head.prev = new_node
        self._heaf = new_node

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
                self._tail = self._curr.prev
                self._curr = self._curr.prev
                return
            elif self._curr.prev is None:
                self._curr.next.prev = None
                self._head = self._curr.next
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
        if self._curr is None or self._curr.next is None:
            return
        else:
            self._curr = self._curr.next

    def move_to_prev(self):
        if self._curr is None or self._curr.prev is None:
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

    def remove_all(self, value):
        node = self._head
        temp_curr = self._curr
        while node is not None:
            if node.data == value:
                if node == self._curr:
                    temp_curr = self._head
                self._curr = node
                self.remove()
            node = node.next
        self._curr = temp_curr

    def reverse(self):
        rev_list = DLL()
        node = self._head
        while node is not None:
            rev_list.insert(node.data)
            node = node.next
        self._head = rev_list._head

    def sort(self):
        node = self._head
        sorted_list = DLL()
        if node.data > node.next.data:
            sorted_list.insert(node.data)
            sorted_list.insert(node.next.data)
        elif node.data <= node.next.data:
            sorted_list.insert(node.next.data)
            sorted_list.insert(node.data)
        node = node.next.next
        while node is not None:
            sorted_list._curr = sorted_list._head
            sorted_node = sorted_list._head
            new_node = Node(node.data)
            while sorted_node is not None:
                if sorted_list._head.data > new_node.data:
                    sorted_list._head.prev = new_node
                    new_node.next = sorted_list._head
                    sorted_list._head = new_node
                    break
                elif sorted_list._tail.data < new_node.data:
                    sorted_list._tail.next = new_node
                    new_node.prev = sorted_list._tail
                    sorted_list._tail = new_node
                    break
                elif sorted_node.data <= new_node.data <= sorted_node.next.data:
                    sorted_list._curr = sorted_node.next
                    sorted_list.insert(new_node.data)
                    break
                else:
                    sorted_node = sorted_node.next
            node = node.next
        self._head = sorted_list._head
