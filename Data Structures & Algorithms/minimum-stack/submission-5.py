class MinStack:

    def __init__(self):
        self.stack = []
        self._min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        curr_min = self._min[-1] if self._min else float('inf')
        new_min = min(val, curr_min)

        self._min.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self._min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min[-1]
