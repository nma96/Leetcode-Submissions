# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # https://www.youtube.com/watch?v=_wUz0XKQ5JM
        self.maximum = float('-inf')
        def dfs(root):
            if root == None: return 0
            left_max = max(0,dfs(root.left))
            right_max = max(0, dfs(root.right))
            
            # remove the below line if the question says path MUST pass through root
            self.maximum = max(self.maximum, left_max + right_max + root.val)
            
            # Directly return below line if path MUST pass through root
            return max(left_max, right_max) + root.val
        dfs(root)
        return self.maximum