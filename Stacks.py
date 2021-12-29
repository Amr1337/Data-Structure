#trying out normal stacks

s = []
s.append("World")
s.append("China")
s.append("Egypt")
s.append("India")

print("Stack before popping items: ", s)

s.pop()
print("Stack after popping items: ", s)

print(s[-1])

#using dequeue
from collections import  deque

stack = deque()

stack.append("World")
stack.append("Egypt")
stack.append("India")
stack.append("Turkey")
print("Stack after append: ", stack)
stack.pop()
print(stack)