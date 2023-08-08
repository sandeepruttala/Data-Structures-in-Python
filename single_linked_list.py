#single linked list
class node:
    def __init__(self, data):
        self.data = data     # assign data
        self.next = None     # the pointer initially points to nothing

class linkedlist:
    def __init__(self):
        self.head = None    # head points to nothing initially
        
#inserting a node at the end of the linked list
    def insert(self, data):
        self.data = data            # assign data
        new_node = node(data)       # create a new node
        if self.head is None:       # if the linked list is empty
            self.head = new_node    # set the head to the new node
            return
        last = self.head            # if the linked list is not empty
        while (last.next):          # iterate to the last node
            last = last.next
        last.next = new_node        # assign the new node to the last node's next

#inserting a node at the beginning of the linked list
    def insert_beginning(self, data):
        self.data = data            # assign data
        new_node = node(data)       # create a new node
        new_node.next = self.head   # set the new node's next to the head
        self.head = new_node        # set the head to the new node
        
#inserting a node at a given position
    def insert_position(self, data, position):
        self.data = data            # assign data
        new_node = node(data)       # create a new node
        if position == 0:           # if the position is 0
            new_node.next = self.head   # set the new node's next to the head
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

#deleting a node
    def delete(self, key):
        temp = self.head                # assign the head to a variable
        if (temp is not None):          # if the linked list is not empty
            if (temp.data == key):      # if the head contains the key
                self.head = temp.next   # set the head to the next node
                temp = None
                return
        while(temp is not None):    # if the linked list is not empty
            if temp.data == key:
                break
            prev = temp             # assign the current node to a variable
            temp = temp.next        # assign the next node to the current node
        if(temp == None):           # if the key is not present in the linked list
            return
        prev.next = temp.next       # set the previous node's next to the next node
        temp = None
#deleting a node at a given position
    def delete_position(self, position):
        if self.head == None:           # if the linked list is empty
            return
        temp = self.head                # assign the head to a variable
        if position == 0:               # if the head is to be deleted
            self.head = temp.next       # set the head to the next node
            temp = None
            return
        for i in range(position - 1):   # iterate to the previous node of the node to be deleted
            temp = temp.next
            if temp is None:            # if the position is more than the number of nodes
                break
        if temp is None:                # if the position is more than the number of nodes
            return
        if temp.next is None:           # if the position is more than the number of nodes
            return
        next = temp.next.next           # assign the next node of the node to be deleted to a variable
        temp.next = None                # set the next node of the node to be deleted to None
        temp.next = next                # set the next node of the previous node to the next node of the node to be deleted

#printing the linked list    
    def printlist(self):
        current = self.head         # assign the head to a variable
        while(current):             # iterate through the linked list
            print(current.data)     # print the data
            current = current.next  # assign the next node to the variable
            
            

#driver code

llist = linkedlist()

llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.insert_beginning(2)
llist.insert_beginning(1)
llist.insert_position(6, 5)
llist.delete(6)
llist.delete_position(4)
llist.printlist()
