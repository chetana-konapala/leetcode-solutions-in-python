class MinStack:

    def __init__(self):
        self._data=[]
        self._mini=[]
        

    def push(self, value: int) -> None:
        self._data.append(value)
        if not self._mini:
            self._mini.append(value)
        else:
            self._mini.append(min(value,self._mini[-1]))
        

    def pop(self) -> None:
        self._data.pop()
        self._mini.pop()
        

    def top(self) -> int:
        return self._data[-1]
        

    def getMin(self) -> int:
        return self._mini[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()