from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0

        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        minute = 0
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for rchg, cchg in directions:
                    new_row = row + rchg
                    new_col = col + cchg

                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
                        fresh -= 1
            minute += 1
        return minute if fresh == 0 else -1