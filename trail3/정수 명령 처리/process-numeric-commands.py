class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0

    def pop(self):
        if self.empty():
            return -1
        return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        if self.empty():
            return -1
        return self.items[-1]

s = Stack()
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "push":
        s.push(int(command[1]))
    elif command[0] == "pop":
        print(s.pop())
    elif command[0] == "size":
        print(s.size())
    elif command[0] == "empty":
        print(s.empty())
    elif command[0] == "top":
        print(s.top())




