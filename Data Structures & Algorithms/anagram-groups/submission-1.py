from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                counts[index] += 1

            key = tuple(counts)

            groups[key].append(word)
        
        return list(groups.values())