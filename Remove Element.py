class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != val:
                nums[index] = nums[i]
                index+=1
        return index