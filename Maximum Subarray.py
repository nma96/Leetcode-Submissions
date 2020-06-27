class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm Nick White
        tempSum = nums[0]
        maxSum = nums[0]
        
        for i in range(1, len(nums)):
            tempSum = max(nums[i], nums[i] + tempSum)
            maxSum = max(maxSum, tempSum)
        
        return maxSum
            