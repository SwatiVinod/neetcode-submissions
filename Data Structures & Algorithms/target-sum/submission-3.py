class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def backtrack(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            if (i, total) in cache:
                return cache[(i, total)]
            
            cache[(i, total)] = (backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i]))
            return cache[(i, total)]
            

        return backtrack(0, 0)