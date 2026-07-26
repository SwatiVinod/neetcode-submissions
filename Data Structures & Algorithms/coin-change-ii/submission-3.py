class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount+1) for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1 # There is 1 way to make 0 amount, Not take the any coins
        
        for i in range(n-1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i+1][a]
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][a]
        

        
