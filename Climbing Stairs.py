class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2] # there is 1 way to climb 1 stair, and 2 ways to climb 2 stairs
        for i in range(2, n): 
            dp.append(dp[i-1]+dp[i-2])
        return dp[n-1]