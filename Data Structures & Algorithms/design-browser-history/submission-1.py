class ListNode: #doubly linked list 
    def __init__(self, url: str):
        self.next = None 
        self.prev = None 
        self.url = url


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    
    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url)
        tmp = self.curr 
        self.curr = self.curr.next
        self.curr.prev = tmp

        
        

    def back(self, steps: int) -> str:
        while self.curr.prev and steps>0:
            self.curr = self.curr.prev
            steps = steps - 1
        return self.curr.url
            

    def forward(self, steps: int) -> str:
        while self.curr.next and steps>0:
            self.curr = self.curr.next
            steps = steps - 1
        return self.curr.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)