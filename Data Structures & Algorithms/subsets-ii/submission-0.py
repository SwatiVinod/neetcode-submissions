class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        n = len(nums)

        def backtrack(i):
            nonlocal path
            result.append(path[:])

            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()

        backtrack(0)
        return result
        