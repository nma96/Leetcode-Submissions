# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None: 
            return l2
        elif l2 is None: 
            return l1
        
        result = ListNode()
        merged = result
        
        while l1 or l2: 
            if l1 is None: 
                merged.next = l2
                break
            elif l2 is None: 
                merged.next = l1
                break
            elif l1.val > l2.val: 
                merged.next = l2
                l2 = l2.next
            else: 
                merged.next = l1
                l1 = l1.next
            
            merged = merged.next
            
        return result.next
            