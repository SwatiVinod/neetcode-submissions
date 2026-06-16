from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = Counter(s)
        t_freq = Counter(t)

        if s_freq == t_freq:
            return True
        else:
            return False
        