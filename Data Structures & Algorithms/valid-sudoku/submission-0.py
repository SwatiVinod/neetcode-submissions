class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        rows_set = [set() for _ in range(rows)]
        cols_set = [set() for _ in range(cols)]
        grid = [set() for _ in range(9)]

        for i in range(rows):
            for j in range(cols):
                grid_num = (i // 3) * 3 + (j // 3)
                if board[i][j] == '.':
                    continue
                value = int(board[i][j])
                if (value not in rows_set[i]) and (value not in cols_set[j]) and (value not in grid[grid_num]):
                    rows_set[i].add(value)
                    cols_set[j].add(value)
                    grid[grid_num].add(value)
                else:
                    return False
        return True


        