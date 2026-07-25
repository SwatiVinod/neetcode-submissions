class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()
        def backtrack(i, path, currentsum):
            if currentsum == target:
                if path[:] not in result:
                    result.append(path[:])
                    return
            
            if currentsum > target or i > n-1:
                return
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                

                path.append(candidates[j])
                currentsum += candidates[j]

                backtrack(j+1, path, currentsum)

                path.pop()
                currentsum -= candidates[j]

        
        backtrack(0, [], 0)
        return result