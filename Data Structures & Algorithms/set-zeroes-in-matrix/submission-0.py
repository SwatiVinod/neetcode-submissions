class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rows_mark = [False] * rows
        cols_mark = [False] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                      rows_mark[i] = True
                      cols_mark[j] = True

        for i in range(rows):
            for j in range(cols):
                if rows_mark[i] or cols_mark[j]:
                    matrix[i][j] = 0
                 