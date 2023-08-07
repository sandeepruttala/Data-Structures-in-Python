#double linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class double_linked_list:
    def __init__(self):
        self.head = None    # head points to nothing initially
#inserting a node at the end of the linked list
    def insert(self, data):
        self.data = data            # assign data
        new_node = Node(data)       # create a new node
        if self.head is None:       # if the linked list is empty
            self.head = new_node    # set the head to the new node
            return
        last = self.head            # if the linked list is not empty
        while (last.next):          # iterate to the last node
            last = last.next
        last.next = new_node        # assign the new node to the last node's next
        new_node.prev = last
#inserting a node at the beginning of the linked list
    def insert_beginning(self, data):
        self.data = data            # assign data
        new_node = Node(data)       # create a new node
        new_node.next = self.head   # set the new node's next to the head
        if self.head is not None:   # if the linked list is not empty
            self.head.prev = new_node
        self.head = new_node        # set the head to the new node
#inserting a node at a given position
    def insert_position(self, data, position):
        self.data = data            # assign data
        new_node = Node(data)       # create a new node
        if position == 0:           # if the position is 0
            new_node.next = self.head   # set the new node's next to the head
            if self.head is not None:   # if the linked list is not empty
                self.head.prev = new_node
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
            if temp.next is not None:       # if the next node of the previous node is not None
                temp.next.prev = new_node
            temp.next = new_node            # set the previous node's next to the new node
            new_node.prev = temp
#deleting a node at a given position
    def delete_position(self, position):
        if self.head is None:           # if the linked list is empty
            return
        temp = self.head                # assign the head to a variable
        if position == 0:               # if the position is 0
            self.head = temp.next       # set the head to the next node of the head
            if self.head is not None:   # if the linked list is not empty
                self.head.prev = None
            temp = None                  # set the previous head to None
            return
        for i in range(position):       # iterate to the node at the position
            temp = temp.next
            if temp is None:            # if the position is more than the number of nodes
                break
        if temp is None:                # if the position is more than the number of nodes
            return
        if temp.next is not None:       # if the next node of the previous node is not None
            temp.next.prev = temp.prev
        if temp.prev is not None:       # if the previous node of the next node is not None
            temp.prev.next = temp.next
        temp = None                     # set the node at the position to None
#deleting a node with a given value
    def delete_value(self, value):
        if self.head is None:           # if the linked list is empty
            return
        temp = self.head                # assign the head to a variable
        if temp.data == value:          # if the head's data is the value
            self.head = temp.next       # set the head to the next node of the head
            if self.head is not None:   # if the linked list is not empty
                self.head.prev = None
            temp = None                  # set the previous head to None
            return
        while temp is not None:         # iterate to the node with the value
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        if temp == None:                # if the value is not found
            return
        prev.next = temp.next           # set the previous node's next to the next node of the node with the value
        if temp.next is not None:       # if the next node of the node with the value is not None
            temp.next.prev = prev
        temp = None                     # set the node with the value to None

#printing the linked list
    def print_list(self):
        temp = self.head                # assign the head to a variable
        while temp is not None:         # iterate to the last node
            print(temp.data, end=" ")
            temp = temp.next
        print()

#driver code
dll = double_linked_list()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.insert(5)
dll.print_list()
dll.insert_beginning(0)
dll.print_list()
dll.insert_position(6, 6)
dll.print_list()