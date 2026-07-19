class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def capture(r, c):
            if (not 0 <= r < rows) or (not 0 <= c < cols) or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)
        
        for r in range(rows):
            if board[r][0] == 'O':
                capture(r, 0)
            if board[r][cols - 1] == 'O':
                capture(r, cols-1)
        
        for c in range(cols):
            if board[0][c] == 'O':
                capture(0, c)
            if board[rows-1][c] == 'O':
                capture(rows-1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        
        