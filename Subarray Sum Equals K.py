class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # https://www.youtube.com/watch?v=bqN9yB0vF08
        
        count = 0
        dictionary = {0:1}
        currSum = 0
        
        for num in nums:
            currSum += num
            if currSum - k in dictionary:
                count += dictionary[currSum-k]
            if currSum in dictionary:
                dictionary[currSum] += 1
            else:
                dictionary[currSum] = 1
        return count