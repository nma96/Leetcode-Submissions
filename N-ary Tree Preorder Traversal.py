"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        output = []
        
        while stack:
            current = stack.pop()
            if current is not None:
                # Use append for preorder traversal
                output.append(current.val)
            
            # Append children in reverse order
            for c in reversed(current.children):
                stack.append(c)
                
        return output