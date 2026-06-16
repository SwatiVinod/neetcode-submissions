class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i, num in enumerate(nums):
            # print(i, num)
            diff = target - num
            # print(diff)
            if diff in dict1.keys():
                return [dict1[diff], i]
            else:
                dict1[num] = i



