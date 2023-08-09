class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} onto the stack")

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f"Popped {item} from the stack")
            return item
        print("Error: Stack underflow")
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        print("Error: Cannot peek from empty stack")
        return None

    def display(self):
        if not self.is_empty():
            print("Stack contents:")
            for item in reversed(self.items):
                print(item)
        else:
            print("Stack is empty")


# driver code

my_stack = Stack()

my_stack.push(5)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.display()
my_stack.pop()
my_stack.display()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.display()
