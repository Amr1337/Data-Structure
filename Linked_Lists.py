class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_in_begining(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "--->"
            itr = itr.next
        print(llstr)

    def insert_in_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_in_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def remove_at(self, index):
        if index <0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count =0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next =itr.next.next
                break
            itr= itr.next
            count+=1

    def insert_at(self, index, data):
        if index <0 or index >=self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.insert_in_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node

            itr = itr.next
            count+=1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data ==data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr= itr.next



    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


ll = LinkedList()
ll.insert_values(["Banana", "mango", "Grapes", "Pomngrate"])
ll.remove_at(2)
print("The length is: ", ll.get_length())

#ll.insert_in_begining(5)
#ll.insert_in_begining(7)
#ll.insert_in_begining(8)
#ll.insert_in_end(15)
ll.insert_at(1,"Figs")
ll.print()
ll.insert_after_value("mango", "apple")
ll.print()
#ll.remove_by_value("Banana")
#ll.remove_by_value("mango")
#ll.remove_by_value("apple")
#ll.remove_by_value("Grapes")
ll.print()