class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return

        if data < self.data:
            #add data to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def in_order_traversal(self):
        elements = []
        #visit left side
        if self.left:
            elements += self.left.in_order_traversal()
        #visit root
        elements.append(self.data)
        #visit right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
               return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BinaryTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return  root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 34, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(20))
    print(numbers_tree.search(12))