class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        area = 0

        left_max = 0
        right_max = 0

        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                area += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                area += right_max - height[right]
                right -= 1
        return area