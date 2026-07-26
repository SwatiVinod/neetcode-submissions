import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        freq = Counter(hand)
        minHeap = list(freq.keys())
        heapq.heapify(minHeap)
        print(minHeap)

        while minHeap:
            first = minHeap[0]

            for num in range(first, first + groupSize):
                if num not in freq:
                    return False
                freq[num] -= 1
                if freq[num] == 0:
                    if num != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True


