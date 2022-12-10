class MyQueue:

    def __init__(self):
        self.s1=[]

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        a=self.s1[0]
        self.s1.pop(0)
        return a
        

    def peek(self) -> int:
        a=self.s1[0]
        return a
        

    def empty(self) -> bool:
        if len(self.s1)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
