# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#the head is the value of the ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        #using tmp variable to not break the link to the chain
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

  


         

        
        
        