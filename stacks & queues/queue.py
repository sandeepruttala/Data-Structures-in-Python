# queue

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item} into the queue")

    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            print(f"Dequeued {item} from the queue")
            return item
        print("Error: Queue underflow")
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        print("Error: Cannot peek from empty queue")
        return None

    def display(self):
        if not self.is_empty():
            print("Queue contents:", end=" ")
            for item in self.items:
                print(item, end=" ")
            print()
        else:
            print("Queue is empty")


# driver code

my_queue = Queue()
my_queue.enqueue(5)
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.dequeue()
my_queue.display()