from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq_t = Counter(t)
        freq_window = {}
        min_length = float('inf')
        have = 0
        need = len(freq_t)
        result = ""

        start = 0
        for end in range(len(s)):
            freq_window[s[end]] = 1 + freq_window.get(s[end], 0)
            
            if s[end] in freq_t and freq_window[s[end]] == freq_t[s[end]]:
                have += 1
            while have == need:
                window_length = end - start + 1

                if window_length < min_length:
                    min_length = window_length
                    result = s[start:end + 1]
                
                freq_window[s[start]] -= 1
                if s[start] in freq_t and freq_window[s[start]] < freq_t[s[start]]:
                    have -= 1
                start += 1

        return result



        
        