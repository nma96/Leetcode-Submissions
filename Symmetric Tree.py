# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.SymmetricHelper(root.left, root.right)
    
    def SymmetricHelper(self, left: TreeNode, right: TreeNode) -> bool:
        
        #Check if either of them are none. If yes, return true if the other is also none
        if left is None or right is None:
            return left == right
        
        if left.val != right.val:
            return False
        
        return self.SymmetricHelper(left.left, right.right) and self.SymmetricHelper(left.right, right.left)