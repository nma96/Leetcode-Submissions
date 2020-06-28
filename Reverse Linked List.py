# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        previous = None
        nextNode = None
        
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        
        return previous