class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # https://www.youtube.com/watch?v=muDPTDrpS28
        reachable = 0
        
        for i in range(len(nums)):
            if reachable < i:
                return False
            reachable = max(reachable, i+nums[i])
        
        return True