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
        
#inserting a node after a given node
    def insert_after(self, prev_node, data):
        self.data = data            # assign data
        new_node = node(data)       # create a new node
        new_node.next = prev_node.next  # set the new node's next to the previous node's next
        prev_node.next = new_node   # set the previous node's next to the new node

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

#printing the linked list    
    def printlist(self):
        current = self.head         # assign the head to a variable
        while(current):             # iterate through the linked list
            print(current.data)     # print the data
            current = current.next  # assign the next node to the variable
            
            

#driver code

llist = linkedlist()

llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)

llist.printlist()
