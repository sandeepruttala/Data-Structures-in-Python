# stack.py
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self, data):
        self.data = data
        if self.top is None:
            self.top = node(data)
            print(f"pushed element {data}")
            return
        new_node = node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"pushed element {data}")

    def pop(self):
        if self.isEmpty():
            print("stack.py underflow")
            return
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        print(f"popped element is {popped_node.data}")

    def peek(self):
        if self.isEmpty():
            print("stack.py underflow")
        print(f"Top is {self.top.data}")

    def display(self):
        if self.isEmpty():
            print("stack.py underflow")
        print("stack.py is: ", end="")
        iter_node = self.top
        while iter_node is not None:
            print(iter_node.data, end=" ")
            iter_node = iter_node.next
        print()

# driver code


my_stack = stack()
my_stack.push(5)
my_stack.peek()
my_stack.push(1)
my_stack.peek()
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.display()
my_stack.pop()
my_stack.peek()
my_stack.display()














