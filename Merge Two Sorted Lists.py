# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        SENTINEL = ListNode(None)
        merged = SENTINEL
        
        while l1 or l2:
            if l1 is None:
                merged.next = l2
                break
            elif l2 is None:
                merged.next = l1
                break
            elif l1.val >= l2.val:
                merged.next = l2
                l2 = l2.next
            else:
                merged.next = l1
                l1 = l1.next
            merged = merged.next
                
        return SENTINEL.next