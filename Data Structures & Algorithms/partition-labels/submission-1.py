class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, char in enumerate(s):
            lastIndex[char] = i

        end = 0
        result = []
        size = 0
        for i, char in enumerate(s):
            end = max(end, lastIndex[char])
            size += 1
            
            if end == i:
                result.append(size)
                end = 0
                size = 0
        return result
