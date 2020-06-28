# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return
        
        midpoint = len(nums)// 2
        node = TreeNode(nums[midpoint])
        
        node.left = self.sortedArrayToBST(nums[:midpoint])
        node.right = self.sortedArrayToBST(nums[midpoint+1:])
        
        return node