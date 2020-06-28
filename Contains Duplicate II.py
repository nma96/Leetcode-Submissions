import math

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary.keys() and abs(i - dictionary[nums[i]])<=k:
                return True
            else:
                dictionary[nums[i]] = i
        return False