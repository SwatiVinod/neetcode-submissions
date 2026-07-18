import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = []
        for stone in stones:
            heapq.heappush(stone_heap, -stone)
        
        while len(stone_heap) > 1:
            stone1 = -heapq.heappop(stone_heap)
            stone2 = -heapq.heappop(stone_heap)

            if stone1 < stone2:
                heapq.heappush(stone_heap, -(stone2 - stone1))
            elif stone2 < stone1:
                heapq.heappush(stone_heap, -(stone1 - stone2))
            
        if stone_heap:
            return -stone_heap[0]
        else:
            return 0
        