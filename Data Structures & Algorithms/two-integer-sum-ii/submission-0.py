class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(numbers)):
            remaining = target - numbers[i]
            if remaining in seen:
                return [seen[remaining] + 1, i+1]
            seen[numbers[i]] = i
        