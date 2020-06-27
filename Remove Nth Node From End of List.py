# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        count = 0
        while(cur):
            count+=1
            cur=cur.next
        
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        location = count - n # 3
        
        while(location):
            location-=1
            cur = cur.next     
        cur.next = cur.next.next
        
        return dummy.next
        
        