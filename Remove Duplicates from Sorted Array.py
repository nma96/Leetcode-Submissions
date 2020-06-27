class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        if len(nums)==0:
            return 0
        for number in range(1,len(nums)):
            if nums[number] != nums[number-1]:
                nums[index] = nums[number]
                index+=1
        return index