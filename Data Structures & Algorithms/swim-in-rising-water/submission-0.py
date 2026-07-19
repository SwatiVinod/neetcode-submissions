import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minheap = [(grid[0][0], 0, 0)]

        visit = set()
        visit.add((0,0))
        directions = [(0,1),(0,-1), (1,0),(-1,0)]

        while minheap:
            t, r, c = heapq.heappop(minheap)

            if r == n-1 and c == n-1:
                return t

            for rchg, cchg in directions:
                new_row = r + rchg
                new_col = c + cchg

                if not ( 0 <= new_row < n) or not ( 0 <= new_col < n) or (new_row, new_col) in visit:
                    continue
                
                visit.add((new_row, new_col))
                heapq.heappush(minheap, (max(t, grid[new_row][new_col]), new_row, new_col))