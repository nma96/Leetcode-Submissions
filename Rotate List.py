# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # empty list
        if not head:
            return head
        
        # finding the length of list and last node to connect
        l = 0
        last = head
        while last.next:
            l+= 1
            last = last.next
        
        # if no roation or mod rotation equal to length then simply return 
        k = k%(l+1)
        if k==0 or k == (l+1):
            return head
        
        # otherwise find the new head
        newhead= head
        i = 0
        while i < l-k:
            newhead = newhead.next
            i+= 1
        
        # reconnect the list to make the rotation
        last.next = head
        head = newhead.next
        newhead.next = None
        
        return head