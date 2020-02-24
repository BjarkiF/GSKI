
class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

def is_ordered(head):
    if head is None:
        return True
    if head.data < head.next.data:          # Nota sér private föll til að skoða öll stökin, byrja á að flokka fyrstu
        head = head.next                    # tvö stökin og sendi svo listana á viðeigandi fall sem fer yfir allan
        ord_check = _is_asc(head)           # listann
        return ord_check
    elif head.data > head.next.data:
        head = head.next
        ord_check = _is_desc(head)
        return ord_check
    elif head.data == head.next.data:
        head = head.next
        is_ordered(head)

def _is_asc(head):
    check = True
    if head.next is not None:              # Tékka hvort allur listinn sé ascending
        if head.data <= head.next.data:
            head = head.next
            _is_asc(head)
        else:
            check = False
    return check

def _is_desc(head):
    check = True
    if head.next is not None:               # Tékka hvort allur listinn sé descending
        if head.data >= head.next.data:
            head = head.next
            _is_desc(head)
        else:
            check = False
    return check

class DLL_Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.curr = None

    def build_lis(self, lis):
        self.head = DLL_Node(lis[0])
        prev = self.head
        for index in range(1, len(lis)):        # bý fyrst til haus með fyrsta stakinu í listanum, fer svo í gegnum
            new_node = DLL_Node(lis[index])     # listann og bý til nýjar nóður og tengi saman jafnóðum
            new_node.prev = prev
            prev.next = new_node
            prev = new_node
        self.tail = new_node
        self.curr = self.head

    def print(self, backwards = False):
        node = self.head
        if backwards:                           # bý til nýjan SLL og set inn í hann það sem kemur út úr DLL, kemur
            rev_lis = SLL()                     # þá í öfugri röð
            while node is not None:
                rev_lis.push_front(node.data)
                node = node.next
            self._print_DLL(rev_lis.head)
        else:
            self._print_DLL(self.head)

    def _print_DLL(self, head):     # Hér er prentað, haft sér til að það sé hægt að prenta upprunalega listann
        node = head                 # án þess að senda hann inn, og lika hægt að senda inn öfuga listann
        ret_str = ''
        while node is not None:
            ret_str += str(node.data) + ' '
            node = node.next
        ret_str = ret_str[:-1]
        print(ret_str)

    def contains(self, item): # Fer í gegnum listann nóðu fyrir nóðu og breakar ef hann finnur item sem stemmir
        node = self.head
        found = False
        while node is not None:
            if node.data == item:
                found = True
                break
            node = node.next
        return found

class SLL:                          # Nota til að setja saman öfugan lista
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_node = SLL_Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("Singly-linked node example:")
    head = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5)))))
    print(str(head))
    print(is_ordered(head))
