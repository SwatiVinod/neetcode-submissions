class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        num_islands = 0

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(row, col):
            if grid[row][col] == "0":
                return

            grid[row][col] = '#'
            for r_chg, c_chg in directions:
                new_row = row + r_chg
                new_col = col + c_chg

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] == "1":
                        dfs(new_row, new_col)
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)
        return num_islands