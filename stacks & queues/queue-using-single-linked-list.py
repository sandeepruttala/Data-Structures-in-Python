# queue

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.data = None
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front is None:
            return True
        return False

    def enqueue(self, data):
        self.data = data
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            print(f'enqueued data: {data}')
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f'enqueued data: {data}')

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        popped_node = self.front
        self.front = self.front.next
        popped_node.next = None
        print(f"dequeued element is {popped_node.data}")

    def peek(self):
        print(f'front is {self.front.data}')

    def display(self):
        print('queue: ', end=" ")
        iter_node = self.front
        while iter_node is not None:
            print(f'{iter_node.data}', end=" ")
            iter_node = iter_node.next
        print()


# driver code
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.dequeue()
queue.display()
queue.peek()
