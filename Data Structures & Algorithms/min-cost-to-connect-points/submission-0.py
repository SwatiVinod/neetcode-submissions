from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        visit = set()

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        result = 0
        minheap = [(0, 0)]
        while len(visit) < n:
            dist, point = heapq.heappop(minheap)
            if point in visit:
                continue
            visit.add(point)
            result += dist

            for neidist, nei in adj[point]:
                if nei not in visit:
                    heapq.heappush(minheap, (neidist, nei))
        return result






