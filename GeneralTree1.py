class TreeNode:
    def __init__(self, name, desgination):
        self.name = name
        self.desgination = desgination
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, input):
        spaces = " " * self.get_level() * 4
        prefix= spaces + "|__" if self.parent else ""

        if input == "name":
            print(prefix + self.name)
            for child in self.children:
                child.print_tree(input)
        elif input == "designation":
            print(prefix + self.desgination)
            for child in self.children:
                child.print_tree(input)
        elif input == "both":
            postfix = " "+ "("+self.desgination+")"
            print(prefix + self.name + postfix)
            for child in self.children:
                child.print_tree(input)




def build_product_tree():

    root_node = TreeNode("Nilupul", "CEO")

    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child((TreeNode("Aamir", "Application Head")))


    hr_head = TreeNode("Gels", "HR Head")
    hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))


    root_node.add_child(cto)
    root_node.add_child(hr_head)

    return root_node

if __name__ == '__main__':
    root_node= build_product_tree()
    #root_node.print_tree("name")
    #root_node.print_tree("designation")
    root_node.print_tree("both")