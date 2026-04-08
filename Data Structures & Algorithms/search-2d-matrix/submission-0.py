class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        
        while left <= right: 
            mid = (left + right) // 2

            if target in matrix[mid]:
                return True
            
            if matrix[mid][0] < target:
                left = mid + 1 
            else:
                right = mid - 1

        return False