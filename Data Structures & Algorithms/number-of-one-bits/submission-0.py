class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            bit_mask = 1 << i
            if bit_mask & n:
                count += 1
        return count 
        