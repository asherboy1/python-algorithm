class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        # print(self.stack == [])
        return self.stack == []

    def push(self,zifu):
        self.stack.append(zifu)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        # print(self.stack(len(self.stack) - 1))
        return self.stack[len(self.stack) - 1]

    def size(self):
        print(len(self.stack))
        return len(self.stack)
