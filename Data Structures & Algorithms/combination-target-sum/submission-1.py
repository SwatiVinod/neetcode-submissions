class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        current_sum = 0
        result = []
        path = []
        
        def backtrack(i):
            nonlocal current_sum
            if current_sum == target:
                result.append(path[:])
                return
            if current_sum > target:
                return
            for j in range(i , n):
                current_sum += nums[j]
                path.append(nums[j])
                backtrack(j)
                path.pop()
                current_sum -= nums[j]
        backtrack(0)
        return result