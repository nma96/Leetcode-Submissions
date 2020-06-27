class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for cur_amount in range(coin, amount+1):
                dp[cur_amount] += dp[cur_amount - coin]
        return dp[-1]