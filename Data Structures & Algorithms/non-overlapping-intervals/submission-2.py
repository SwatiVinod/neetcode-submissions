class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[0])
        remove_count = 0

        prev_end = float('-inf')
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
                continue
            else:
                remove_count += 1
                prev_end = min(prev_end, end)
        return remove_count

