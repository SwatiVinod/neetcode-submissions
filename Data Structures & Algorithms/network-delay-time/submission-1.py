from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        visit = set()

        t = 0

        while minHeap:
            w1, u1 = heapq.heappop(minHeap)
            if u1 in visit:
                continue
            
            t = max(t, w1)
            visit.add(u1)
            for u2, w2 in edges[u1]:
                if u2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, u2))
    
        return t if len(visit) == n else -1
        