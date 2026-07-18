class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            sum_of_squares = 0
            while n != 0:
                digit = n % 10
                sum_of_squares += digit * digit
                n = n // 10
            if sum_of_squares not in seen:
                seen.add(sum_of_squares)
            else:
                return False
            n = sum_of_squares
        return True

        