class Solution:
    def isPalindrome(self, string, l , r):
        while l < r:
            if string[l] != string[r]:
                return False
            l, r = l+1, r-1
        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def bactrack(i):
            if i >= len(s):
                result.append(path[:])
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    path.append(s[i:j+1])
                    bactrack(j + 1)
                    path.pop()
        bactrack(0)
        return result
        
