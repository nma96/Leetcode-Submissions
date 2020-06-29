class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # https://www.youtube.com/watch?v=kssIQAIg9c8&t=2s
        k = self.kadane(A)
        
        CS = 0
        for i in range(len(A)):
            CS += A[i]
            A[i] = -A[i]
        CS = CS + self.kadane(A)
        
        if CS > k and CS != 0:
            return CS
        else:
            return k
        
    def kadane(self, nums):
        curSum, maxSum = nums[0], nums[0]
        for n in nums[1:]:
            curSum = max(n, curSum+n)
            maxSum = max(curSum, maxSum)
        return maxSum