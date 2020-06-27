class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i,number in enumerate(nums):
            temp = target - number
            if temp in comp:
                return comp[temp], i
            comp[number] = i
            