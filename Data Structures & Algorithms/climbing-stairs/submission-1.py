class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        dp_array = [-1] * (n+1)
        dp_array[1] = 1
        dp_array[2] = 2

        for i in range(3, n+1):
            dp_array[i] = dp_array[i-1] + dp_array[i-2]
        return dp_array[n]

        
