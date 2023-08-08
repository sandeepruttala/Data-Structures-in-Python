#circular linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circular_linked_list:
    def __init__(self):
        self.head = None    # head points to nothing initially
        
#inserting a node at the end of the linked list
    def insert(self, data):
        self.data = data            # assign data
        new_node = node(data)       # create a new node
        if self.head is None:       # if the linked list is empty
            self.head = new_node    # set the head to the new node
            new_node.next = self.head
            return
        last = self.head            # if the linked list is not empty
        while (last.next != self.head):          # iterate to the last node
            last = last.next
        last.next = new_node        # assign the new node to the last node's next
        new_node.next = self.head
#inserting a node at the beginning of the linked list
    def insert_beginning(self, data):
        self.data = data            # assign data
        new_node = node(data)       # create a new node
        new_node.next = self.head   # set the new node's next to the head
        if self.head is None:       # if the linked list is empty
            new_node.next = new_node
        else:
            last = self.head        # if the linked list is not empty
            while (last.next != self.head):          # iterate to the last node
                last = last.next
            last.next = new_node
        self.head = new_node        # set the head to the new node
#inserting a node at a given position
    def insert_position(self, data, position):
        self.data = data            # assign data
        new_node = node(data)       # create a new node
        if position == 0:           # if the position is 0
            new_node.next = self.head   # set the new node's next to the head
            if self.head is None:       # if the linked list is empty
                new_node.next = new_node
            else:
                last = self.head        # if the linked list is not empty
                while (last.next != self.head):          # iterate to the last node
                    last = last.next
                last.next = new_node
            self.head = new_node        # set the head to the new node
        else:
            temp = self.head            # assign the head to a variable
            for i in range(position - 1):   # iterate to the previous node of the position
                temp = temp.next
                if temp is None:            # if the position is more than the number of nodes
                    break
            if temp is None:                # if the position is more than the number of nodes
                return
            new_node.next = temp.next       # set the new node's next to the next node of the previous node
            temp.next = new_node            # set the previous node's next to the new node
#deleting a node at the end of the linked list
    def delete(self):
        if self.head is None:           # if the linked list is empty
            return
        if self.head.next is None:      # if the linked list has only one node
            self.head = None
            return
        last = self.head                # if the linked list has more than one node
        while (last.next.next != self.head):        # iterate to the second last node
            last = last.next
        last.next = self.head           # set the second last node's next to the head
#deleting a node at the beginning of the linked list
    def delete_beginning(self):
        if self.head is None:           # if the linked list is empty
            return
        if self.head.next is None:      # if the linked list has only one node
            self.head = None
            return
        last = self.head                # if the linked list has more than one node
        while (last.next != self.head):         # iterate to the last node
            last = last.next
        last.next = self.head.next      # set the last node's next to the second node
        self.head = self.head.next      # set the head to the second node
#deleting a node at a given position
    def delete_position(self, position):
        if self.head is None:           # if the linked list is empty
            return
        if position == 0:               # if the position is 0
            if self.head.next is None:      # if the linked list has only one node
                self.head = None
                return
            last = self.head                # if the linked list has more than one node
            while (last.next != self.head):         # iterate to the last node
                last = last.next
            last.next = self.head.next      # set the last node's next to the second node
            self.head = self.head.next      # set the head to the second node
        else:
            temp = self.head            # assign the head to a variable
            for i in range(position - 1):   # iterate to the previous node of the position
                temp = temp.next
                if temp is None:            # if the position is more than the number of nodes
                    break
            if temp is None:                # if the position is more than the number of nodes
                return
            temp.next = temp.next.next       # set the previous node's next to the next node of the next node
#displaying the linked list
    def display(self):
        if self.head is None:           # if the linked list is empty
            return
        temp = self.head                # assign the head to a variable
        while (temp.next != self.head):         # iterate to the last node
            print(temp.data, end = " ")
            temp = temp.next
        print(temp.data, end = " ")
        print()

#driver code
cll = circular_linked_list()
cll.insert(1)
cll.insert(2)
cll.insert(3)
cll.insert(4)
cll.insert(5)
cll.display()
cll.insert_beginning(0)
cll.display()
cll.insert_position(6, 6)
cll.display()
cll.delete()