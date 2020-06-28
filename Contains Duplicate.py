class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for i in nums:
            if i in dictionary:
                return True
            else:
                dictionary[i] = i
        return False