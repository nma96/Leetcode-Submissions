# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)
        
        return max(right, left) + 1