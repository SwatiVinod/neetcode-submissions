from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        l = r = 0
        output = []

        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()

            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if (r - l) + 1 >= k:
                output.append(nums[queue[0]])
                l += 1
            r += 1
        return output


        
