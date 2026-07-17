class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(0,1), (0,-1), (1,0),(-1,0)]

        def dfs(row, col, visited, prevHeight):
            visited.add((row, col))
            
            original_height = heights[row][col]
            for r_chg, c_chg in directions:
                new_row = row + r_chg
                new_col = col + c_chg

                if 0 <= new_row < rows and 0 <= new_col < cols and heights[new_row][new_col] >= heights[row][col] and (new_row, new_col) not in visited:
                    
                    dfs(new_row, new_col, visited, heights[row][col])
            return

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])

        intersection = list(pacific.intersection(atlantic))
        print(pacific)
        print(atlantic)
        print(intersection)
        result = []
        for row, col in intersection:
            result.append([row, col])
        return result


        