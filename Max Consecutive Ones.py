class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            elif i == 0:
                res = max(count, res)
                count = 0
        return max(count,res)