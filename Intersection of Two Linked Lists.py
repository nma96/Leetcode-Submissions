# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hash_table_A = {}
        while headA != None:
            hash_table_A[headA] = headA.next
            headA = headA.next
        while headB != None:
            if headB in hash_table_A:
                return headB
            headB = headB.next
        return None
            