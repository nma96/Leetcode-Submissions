"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        output = []
        while stack:
            current = stack.pop()
            if current is not None:
                output.insert(0,current.val)
            for c in current.children:
                stack.append(c)
                
        return output