class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
           print("Empty")
           return

        itr = self.head
        llstr =""
        while itr:
            llstr += str(itr.data)
            itr = itr.next
        print(llstr)

    def insert_at_begining(self, data):
        node = Node(data,self.head)
        self.head = node


ll= LinkedList()
#ll.add_value(1)(["Amr", "Mohamed", "Abdelazeem"])

ll.print()