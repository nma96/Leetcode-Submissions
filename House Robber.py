class Solution:
    def rob(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=xlvhyfcoQa4
        n = len(nums)
        
        # Edge Cases
        if nums is None or n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        
        # Main case (MaxMoney until current house)
        # Initializations 
        maxMoney = [0]*n
        maxMoney[0] = nums[0]
        maxMoney[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            maxMoney[i] = max(nums[i] + maxMoney[i-2], maxMoney[i-1])
        
        return maxMoney[n-1]