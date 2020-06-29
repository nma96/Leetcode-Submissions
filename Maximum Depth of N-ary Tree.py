"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            # empty node or empty tree
            return 0
    
        else:
            # DFS to choose the longest path
            
            if root.children:
                # current node has subtrees
                return max( self.maxDepth(child) for child in root.children ) + 1
            
            else:
                # current node is leaf node
                return 1