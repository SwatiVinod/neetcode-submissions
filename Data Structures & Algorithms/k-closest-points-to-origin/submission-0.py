import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        result = []

        for x, y in points:
            distancesq_to_origin = x*x + y*y
            heapq.heappush(closest_points, (-distancesq_to_origin, (x, y)))

            if len(closest_points) > k:
                heapq.heappop(closest_points)
            
        for i in range(len(closest_points)):
            result.append(closest_points[i][1])

        return result

