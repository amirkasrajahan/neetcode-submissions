class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowToSearch = 0
        
        while target > matrix[rowToSearch][len(matrix[rowToSearch]) - 1]:
            rowToSearch += 1
            if rowToSearch == len(matrix): return False
        low, high = 0, len(matrix[rowToSearch]) - 1

        while low <= high:
            mid = (high + low) // 2
            if target == matrix[rowToSearch][mid]:
                return True
            elif target < matrix[rowToSearch][mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        return False