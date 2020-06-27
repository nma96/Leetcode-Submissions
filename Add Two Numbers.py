# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Declare pointers for traversal. Added for clarity.
        p1 = l1
        p2 = l2

        # Declare current carry over.
        currentCarry = 0

        # Declare cur variable to help traverse and add nodes to new list.
        # Declare head variable to be the head of the list.
        head = cur = ListNode(0)

        # Iteration condition.
        while p1 or p2 or currentCarry:

            # print(p1.val, p2.val, currentCarry)

            # Determine current value and carry over.
            currentVal = currentCarry
            currentVal += 0 if p1 is None else p1.val
            currentVal += 0 if p2 is None else p2.val
            if currentVal >= 10:
                currentVal -= 10
                currentCarry = 1
            else:
                currentCarry = 0

            # print(currentVal, currentCarry)

            # Add current value as it will always atleast be '1'.
            cur.next = ListNode(currentVal)
            cur = cur.next

            # Add base cases for iterating linked lists.
            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next
            elif p2 is None:
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next

        # Return next node.
        return head.next