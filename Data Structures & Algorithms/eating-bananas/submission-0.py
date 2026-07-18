class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            k = (left + right) // 2

            max_time = 0
            for p in piles:
                max_time += math.ceil(float(p) / k)
            if max_time <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result