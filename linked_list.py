class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    empty_msg = "linked list is empty"

    def __init__(self):
        self.head = None

    def __str__(self):
        nd_list = []
        if self.head:
            current = self.head
            while current:
                nd_list.append(current.data)
                current = current.next
        return str(nd_list)

    def size(self):
        ''' return the size of the linked list '''
        count = 0
        if self.head:
            current = self.head
            while current:
                count += 1
                current = current.next
        return count

    def append(self, data):
        ''' append node to the end of linked list '''
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def add(self, data):
        ''' add new node to the front of linked list '''
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode

    def search(self, item) -> bool:
        ''' search for item in list.
           return True if found, False otherwise '''
        current = self.head
        while current:
            if current.data is item:
                return True
            else:
                current = current.next
        return False

    def pop(self):
        ''' remove first node from linked list '''
        try:
            item = self.head.data
            self.head = self.head.next
            print(f'{item} removed')
        except AttributeError:
            print(self.empty_msg)

    def remove(self, item):
        ''' remove the item from linked list.
           ONLY the first occurrence of the item is removed '''
        try:
            if self.head.data is item:
                self.pop()
            else:
                current = self.head
                while current.next:
                    if current.next.data is item:
                        current.next = current.next.next
                        print(f'{item} removed')
                        return
                    else:
                        current = current.next
                print(f'{item} not found')
        except AttributeError:
            print(self.empty_msg)
