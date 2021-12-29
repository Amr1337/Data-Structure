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
    def find_min(self):
        min_element = self.in_order_traversal()
        return min(min_element)

    def find_max(self):
        max_element = self.right.in_order_traversal()
        return max(max_element)

    def calculate_sum(self):
        sum = 0
        for i in self.in_order_traversal():
            sum+= i
        return sum

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
def build_tree(elements):
    root = BinaryTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return  root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 34, 18, 34, 18, 4]
    number_tree = build_tree(numbers)
    #print("The Minimum element in the tree: ", number_tree.find_min())
    #print("The Maximum element in the tree: ", number_tree.find_max())
    #print("Sum of the tree elements: "number_tree.calculate_sum())
    print(number_tree.pre_order_traversal())
    print(number_tree.post_order_traversal())
