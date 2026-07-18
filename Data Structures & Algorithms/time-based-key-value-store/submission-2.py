from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        left = 0
        right = len(self.timemap[key]) -1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2

            value, ex_timestamp = self.timemap[key][mid]

            if ex_timestamp <= timestamp:
                result = value
                left = mid + 1
            else:
                right = mid - 1
        return result
        

