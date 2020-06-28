class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.minStack = []

    def push(self, x: int) -> None:
        if self.minStack == []:
            self.minStack.append(x)
        elif self.minStack[-1] >= x:
            self.minStack.append(x)
        self.items.append(x)
        

    def pop(self) -> None:
        temp = self.items.pop()
        if temp == self.minStack[-1]:
            self.minStack.pop()
        return temp
    

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minStack[-1] # Constant time. Using min() is O(n)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()