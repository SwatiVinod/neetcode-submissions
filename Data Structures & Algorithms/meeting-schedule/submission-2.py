"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        n = len(intervals)
        attended = 1

        if n == 0:
            return True

        prev_end = intervals[0].end
        for interval in intervals[1:]:
            if interval.start >= prev_end:
                attended += 1
                prev_end = interval.end
        
        return attended == n

