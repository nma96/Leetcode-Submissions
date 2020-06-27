# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # def helper(root):
        #     if root:
        #         helper(root.left)
        #         helper(root.right)
        #         res.append(root.val)
        # helper(root)
        # return res
    
        # Iterative
        if not root:
            return None
        if not root.left and not root.right:
            return [root.val]
        
        # DFS Solution
        # Reverse Preorder
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]