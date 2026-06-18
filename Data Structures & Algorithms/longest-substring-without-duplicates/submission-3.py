class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1 = {}
        l = 0

        result = 0

        for r in range(len(s)):
            if s[r] in dict1:
                l = max(dict1[s[r]] + 1, l)
            result = max(result, r - l + 1)
            dict1[s[r]] = r
        return result
            
