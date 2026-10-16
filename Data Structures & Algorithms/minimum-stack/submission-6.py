class MinStack:

    def __init__(self, capacity: int = 30000):
        self.stack = [None] * capacity
        self.min = [None] * capacity
        self.size = 0        # number of items in stack
        self.min_size = 0    # number of items in min
        self.capacity = capacity

    def push(self, val: int) -> None:
        if self.size == self.capacity:
            raise OverflowError("stack is full")
        self.stack[self.size] = val
        self.size += 1
        if self.min_size == 0 or val <= self.min[self.min_size - 1]:
            self.min[self.min_size] = val
            self.min_size += 1

    def pop(self) -> None:
        if self.size == 0:
            raise IndexError("pop from empty stack")
        self.size -= 1
        if self.stack[self.size] == self.min[self.min_size - 1]:
            self.min_size -= 1

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.min[self.min_size - 1]