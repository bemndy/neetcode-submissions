class MinStack:

    def __init__(self):
        self.data = []
        self.min = None

    def push(self, val: int) -> None:
        self.data.append(val)
        self.min = min(self.data)

    def pop(self) -> None:
        self.data.pop()
        if self.data:
            self.min = min(self.data)

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()