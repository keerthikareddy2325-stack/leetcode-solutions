class MyStack:
    def __init__(self):
        self.dq1=deque()
        self.dq2=deque()
    def push(self, x: int) -> None:
        while len(self.dq1)>0:
            self.dq2.append(self.dq1.pop())
        self.dq1.append(x)
        while len(self.dq2)>0:
            self.dq1.append(self.dq2.pop())
    def pop(self) -> int:
        return self.dq1.popleft()
    def top(self) -> int:
        return self.dq1[0]
    def empty(self) -> bool:
        if len(self.dq1)==0:
            return True
        else:
            return False
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()