class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        n = len(nums)
        pick = [False] * len(nums)
        def backtrack(i):
            nonlocal path
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for j in range(n):
                if not pick[j]:
                    path.append(nums[j])
                    pick[j] = True
                    backtrack(j+1)
                    path.pop()
                    pick[j] = False

        backtrack(0)
        return result

        
