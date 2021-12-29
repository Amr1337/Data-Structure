class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def itterate_items(self):
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def append_items(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
           self.head = node
           self.tail = node
        self.count+=1


items = LinkedList()
items.append_items("PHP")
items.append_items("Java")
items.append_items("Python")
items.append_items("C#")

for val in items.itterate_items():
    print(val)
print("\n")
print(items.count)
print(items.head.data)
print(items.tail.data)
