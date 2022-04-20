class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        reqCount = len(nums)//2
        for i in range(len(nums)):
            if nums[i] in count: 
                count[nums[i]] += 1
                if count[nums[i]] > reqCount: 
                    return nums[i]
            else: 
                count[nums[i]] = 1
                if count[nums[i]] > reqCount: 
                    return nums[i]