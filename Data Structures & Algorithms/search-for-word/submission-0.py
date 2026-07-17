class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(0,1), (0,-1), (-1,0), (1,0)]

        def backtrack(row, col, i):
            if i == len(word):
                return True

            # Invalid position or character mismatch
            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != word[i]
            ):
                return False
            
            original_char = board[row][col]
            board[row][col] = '#'

            for r_chg, c_chg in directions:
                new_row = row + r_chg
                new_col = col + c_chg

                if backtrack(new_row, new_col, i + 1):
                    board[row][col] = original_char
                    return True

            board[row][col] = original_char
            return False

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False
