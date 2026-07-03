class MinStack:

    def __init__(self):
        self.stack1 = [] #initializing stack1 as a list
        self.tracker = []
        

    def push(self, val: int) -> None: #not returning anything
        self.stack1.append(val)

        if self.tracker != []:
            self.tracker.append(min(val,self.tracker[-1]))
        else:
            self.tracker.append(val)

    
    def pop(self) -> None:
        self.stack1.pop()
        self.tracker.pop()
        

    def top(self) -> int:
        return self.stack1[-1]
        

    def getMin(self) -> int:
        return self.tracker[-1]



        
