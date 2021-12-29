class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level =0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, tree_level):
        if self.get_level() > tree_level:
            return

        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(tree_level)


def build_location_tree():
    global_node = TreeNode("Global")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))
    india = TreeNode("India")
    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    new_jeresy =TreeNode("New Jersey")
    new_jeresy.add_child(TreeNode("Princeton"))
    new_jeresy.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(new_jeresy)
    usa.add_child(california)

    global_node.add_child(india)
    global_node.add_child(usa)

    return global_node

if __name__ == '__main__':
    global_node = build_location_tree()
    global_node.print_tree(3)