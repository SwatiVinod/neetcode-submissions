class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows_set = set()
        cols_set = set()
        diagonals = set()
        anti_diagonals = set()
        placed = 0

        result = []

        chess_board = [['.'] * n for _ in range(n)]

        def convert_to_string(chess_board):
            chess_string = []
            for i in range(n):
                chess_string.append("".join(chess_board[i]))
            return chess_string

        def backtrack(row):
            nonlocal placed
            nonlocal result
            
            for col in range(n):
                if row not in rows_set and col not in cols_set and (row + col) not in diagonals and (row - col) not in anti_diagonals:
                    rows_set.add(row)
                    cols_set.add(col)
                    diagonals.add(row + col)
                    anti_diagonals.add(row - col)
                    chess_board[row][col] = 'Q'
                    placed += 1

                    if placed == n:
                        chess_board_string = convert_to_string(chess_board)
                        result.append(chess_board_string)

                    backtrack(row+1)

                    placed -= 1
                    rows_set.remove(row)
                    cols_set.remove(col)
                    diagonals.remove(row + col)
                    anti_diagonals.remove(row - col)
                    chess_board[row][col] = '.'
        backtrack(0)
        return result