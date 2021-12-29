import time
from collections import deque
import threading
from threading import Thread

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        return self.buffer.append(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

food_ordering = Queue()
def place_oder(order):
    for o in order:
        food_ordering.enqueue(o)
        time.sleep(0.5)
        print("New Order: ",o)

def serve_order(order):
    time.sleep(1)
    for o in order:
        food_ordering.dequeue()
        time.sleep(2)
        print("Order ready:", o)

orders = ['pizza','samosa','pasta','biryani','burger']

place_order = Thread(target=place_oder, args=(orders,))
serve_order = Thread(target=serve_order, args=(orders,))

place_order.start()
serve_order.start()

#place_order.join()
#serve_order.join()
#print(threading.active_count())
#print(food_ordering.size())
