class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            # print(left)
            # print(right)

            mid = (left + right) // 2
            # print("mid")
            # print(mid)
            if nums[mid] > nums[mid + 1]:
                if nums[mid] > nums[right]:
                    return nums[mid + 1]
                else:
                    right = mid
            else:
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid  
        return nums[left]             