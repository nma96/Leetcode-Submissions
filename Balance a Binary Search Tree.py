# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            """inorder depth-first traverse bst"""
            if not node: return 
            dfs(node.left)
            value.append(node.val)
            dfs(node.right)
        
        value = [] #collect values
        dfs(root)
        
        def tree(lo, hi): 
            if lo > hi: return None
            mid = (lo + hi)//2
            ans = TreeNode(value[mid])
            ans.left = tree(lo, mid-1)
            ans.right = tree(mid+1, hi)
            return ans
        
        return tree(0, len(value)-1)
    
    # T - O(n)
    # S - O(n)