from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = []
        self.pointCounts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append((point[0], point[1]))
        self.pointCounts[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point
        for x, y in self.points:
            if (abs(px - x) != abs(py - y)) or x == px or y ==py:
                continue
            result += self.pointCounts[(x, py)] * self.pointCounts[(px, y)]
        return result

        
