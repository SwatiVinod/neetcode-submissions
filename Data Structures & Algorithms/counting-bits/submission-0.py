class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n+1):
            count = 0
            for i in range(32):
                bit_mask = 1 << i
                if bit_mask & num:
                    count += 1
            result.append(count)
        return result