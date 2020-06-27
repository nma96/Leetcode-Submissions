from queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Create a minHeap pririty Queue  
        # put all the values of all the lists into it
        minHeap = PriorityQueue()
        for head in lists:
            while head != None:
                minHeap.put(head.val)
                head = head.next
        
        # Create new list and keep adding the minHeap top elements
        dummy = head = ListNode(-1)
        
        while not minHeap.empty():
            head.next = ListNode(minHeap.get())
            head = head.next
        return dummy.next

        
        # Run Time: O(n*m log(n*m))
        # Space: O(n*m)
        
        # n = max # of lists; m = max # of nodes in list