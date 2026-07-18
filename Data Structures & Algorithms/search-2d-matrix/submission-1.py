class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        rows = len(matrix)
        cols = len(matrix[0])
        target_row = -1

        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                target_row = mid
                break
            elif target > matrix[mid][cols - 1]:
                top = mid + 1
            else:
                bottom = mid - 1
        
        if target_row == -1:
            return False
        
        left = 0
        right = cols -1

        while left <= right:
            mid = (left + right) // 2
            if target == matrix[target_row][mid]:
                return True
            elif target > matrix[target_row][mid]:
                left = mid + 1
            else:
                right = mid - 1
            
        return False

        