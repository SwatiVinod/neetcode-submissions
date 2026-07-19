class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        path = []

        def backtrack(digit):
            nonlocal path
            if len(path) == len(digits):
                result.append("".join(path))
                return
            for char in digit_to_letter[digits[digit]]:
                path.append(char)
                backtrack(digit + 1)
                path.pop()
        backtrack(0)
        return result