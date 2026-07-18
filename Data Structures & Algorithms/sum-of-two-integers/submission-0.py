class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_signed_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        if a < max_signed_int:
            return a
        else:
            return a - (1<<32)
        