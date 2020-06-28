class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = 2**31
        profit = 0
        
        for i in range(len(prices)):
            if prices[i] < minVal:
                minVal = prices[i]
            else:
                profit = max(profit, prices[i] - minVal)
            
        return profit