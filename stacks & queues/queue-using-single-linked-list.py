#queue

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.data = None
        self.front = None
        self.rear = None

    def enqueue(self,data):
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
        pass