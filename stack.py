class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

#no need to implement stack in python lol

#bracket balancing

def isBalanced(s):
    table = {')': '(', ']': '[', '}': '{'}

    for _ in range(len(s)):
        stack = []
        for x in s:
            if stack and table.get(x) == stack[-1]:
                stack.pop()
            else:
                stack.append(x)
        return "NO" if stack else "YES"





