# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
    
        # Recursion
#        return self.validate(root, None, None)
#   
#    
#   def validate(self, root: TreeNode, max: int, min: int) -> bool:
#        if root is None:
#            return True
#        elif max != None and root.val >= max or min != None and root.val <= min:
#            return False
#        else:
#            return self.validate(root.left, root.val, min) and self.validate(root.right, max, root.val)