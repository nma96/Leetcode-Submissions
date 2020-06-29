class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = set(nums)
        length = len(nums) + 1

        for i in range(length):
            if i not in temp:
                return i