
class ListNode: 
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0) #dummy head exists so as to not have a null head pointer 
        self.size = 0 #to quickly validate indices without having to traverse the entire list || assume 0-indexing || dummy node doesnt count in size 

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
    
        curr = self.head.next
        tracker = index
        while tracker > 0:
            curr = curr.next
            tracker = tracker - 1
        return curr.val #remember to return the actual integer


    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        tmp = self.head.next 
        self.head.next = newNode
        newNode.next = tmp 
        self.size = self.size + 1 #remember to increment size 

                

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        curr = self.head
        for _ in range(self.size):
            curr = curr.next
        curr.next = newNode
        self.size = self.size + 1 #increment size 
            
        
    def addAtIndex(self, index: int, val: int) -> None:
        #questions to consider: what if the index is out of bounds? do nothing! from problem statement: index can equal the size! thats why we have > as opposed ot >= in the conditional
        #                       what happens to the size of the linked list?                       
        if index > self.size:   
            return 

        newNode = ListNode(val)
        curr = self.head 
        for _ in range(index):
            curr = curr.next
        newNode.next = curr.next
        curr.next = newNode #no tmp needed || line 52 MUST come first or else we'll break the link to the rest of the list 
        
        self.size = self.size + 1 

        

    def deleteAtIndex(self, index: int) -> None:
        #remember to check if index is valid! 
        if index >= self.size or index < 0: 
            return


        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next  = curr.next.next
        self.size = self.size - 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)