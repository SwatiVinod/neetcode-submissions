"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        n = len(intervals)
        if n == 0:
            return 0

        end_times = []
        num_rooms = 1
        heapq.heappush(end_times, intervals[0].end)

        for interval in intervals[1:]:
            last_meeting_end_time = end_times[0]

            if last_meeting_end_time > interval.start:
                num_rooms += 1
            if end_times and last_meeting_end_time <= interval.start:
                heapq.heappop(end_times)
            
            heapq.heappush(end_times, interval.end)
        return num_rooms
        

    