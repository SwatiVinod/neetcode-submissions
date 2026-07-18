class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        result = [intervals[0]]

        for start, end in intervals:
            last_end = result[-1][1]

            if last_end >= start:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])
            
        return result

        