# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        val = 0
        length = 0
        arr = ''
        
        while head != None:
            arr += str(head.val)
            length +=1
            head = head.next
        
        for i in range(len(arr)):
            val += int(arr[i])*(2**(length-1))
            length -= 1
        
        return val