from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

def get_reverse(str):
    stack = Stack()
    for ch in str:
        stack.push(ch)
    rstr=""
    while stack.size()!=0:
        rstr += stack.pop()
    return rstr

def is_balanced(str):
    stack = Stack()
    for ch in str:

        if (ch == "(" or ch == "{") or ch == "[":
            stack.push(ch)
        elif (ch == ")" or ch == "}") or ch == "]":
            if stack.size() == 0:
                return False
            else:
                stack.pop()
                return True


#reverse_string = "We will conquere COVID-19"
#print(get_reverse(reverse_string))
s = Stack()

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
