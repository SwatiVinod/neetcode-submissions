import heapq
class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []
        
    def addNum(self, num: int) -> None:
        if not self.small_heap or num <= -self.small_heap[0]:
            heapq.heappush(self.small_heap, -num)
        else:
            heapq.heappush(self.large_heap, num)
        self.rebalance()

    def rebalance(self):
        if len(self.small_heap) > len(self.large_heap) + 1:
            val = heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, -val)
        if len(self.large_heap) > len(self.small_heap):
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -val)

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            return -self.small_heap[0]
        else:
            return (-self.small_heap[0] + self.large_heap[0]) / 2
        