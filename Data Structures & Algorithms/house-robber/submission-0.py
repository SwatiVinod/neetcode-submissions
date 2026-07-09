class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp_array = [-1] * len(nums)
        # dp_array[0] = nums[0]
        # dp_array[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     dp_array[i] = max(nums[i] + dp_array[i-2], dp_array[i-1])
        # return dp_array[-1]

        # Space opitimized

        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2



        