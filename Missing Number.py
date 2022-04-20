class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)): 
            dict[nums[i]] = 1
        
        for i in range(len(nums)+1):
            if i in dict: 
                del dict[i]
            else:
                return i
            