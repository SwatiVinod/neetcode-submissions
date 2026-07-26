class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n-1, -1, -1):
            for buy in [True, False]:
                if buy:
                    buy = dp[i+1][False] - prices[i] if i+1 < n else -prices[i]
                    cooldown = dp[i+1][True]
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i+2][True] + prices[i] if i+2 < n else prices[i]
                    cooldown = dp[i+1][False]
                    dp[i][0] = max(sell, cooldown)
        
        print(dp)
        return dp[0][1]
