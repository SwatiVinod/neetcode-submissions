class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(1, len(nums) + 1):
            result = result ^ i
        for num in nums:
            result = result ^ num
        return result
