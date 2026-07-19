from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        inf = 2147483647
        result = [[-1] * cols for _ in range(rows)]

        def bfs(row, col):
            queue = deque([(row, col)])
            steps = 0
            visit = [[False] * cols for _ in range(rows)]
            visit[row][col] = True
            
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if grid[r][c] == 0:
                        return steps
                    for rchg, c_chg in directions:
                        new_row = r + rchg
                        new_col = c + c_chg

                        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != -1 and not visit[new_row][new_col]:
                            visit[new_row][new_col] = True
                            queue.append((new_row, new_col))
                steps += 1
            return inf

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == inf:
                    shortest_path = bfs(i, j)
                    grid[i][j] = shortest_path


