class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(row, col):
            
            grid[row][col] = 0
            area = 1
            for rchg, cchg in directions:
                new_row = rchg + row
                new_col = cchg + col

                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                    area += dfs(new_row, new_col)
            return area


        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)
        return max_area
