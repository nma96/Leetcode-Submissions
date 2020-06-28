# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Check for the head. If the list is 6->6->6->1->2->3, the t
        while head != None and head.val == val:
            head = head.next
        
        # After the check is done and head is no longer the required value, set new head to current
        current = head
        
        # Traverse through the linked list and when the next value is val, make current.next = current.next.next.
        while current != None and current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
            
        return head