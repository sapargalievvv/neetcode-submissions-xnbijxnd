class MinStack:

    def __init__(self):
        self.stack = []
        self.minEl = 99999999999

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minEl = min(self.minEl, val)

    def pop(self) -> None:
       self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if len(self.stack):
            return min(self.stack)
