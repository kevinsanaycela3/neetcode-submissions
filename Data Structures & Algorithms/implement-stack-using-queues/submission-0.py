class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q2.append(x)
        while len(self.q1) != 0:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
 

    def pop(self) -> int:
        if self.q1:
            return self.q1.popleft()
        

    def top(self) -> int:
        if self.q1:
            return self.q1[0]
        

    def empty(self) -> bool:
        if len(self.q1) == 0:
             return True 
        else:
             return False