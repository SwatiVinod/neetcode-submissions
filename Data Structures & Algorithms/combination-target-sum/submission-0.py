class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        current_sum = 0
        start = 0
        path = []
        
        def backtrack(start):
            nonlocal current_sum
            if current_sum == target:
                result.append(path[:])
                return
            if current_sum > target:
                return
            for i in range(start, n):
                current_sum += nums[i]
                path.append(nums[i])
                backtrack(i)
                path.pop()
                current_sum -= nums[i]
        
        backtrack(start)
        return result