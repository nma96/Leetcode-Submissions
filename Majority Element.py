class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = collections.OrderedDict()
        n = len(nums)//2
        
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        
        for i in range(len(nums)):
            if dict[nums[i]] > n:
                return nums[i]