class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])

        for row in matrix:
            low, high = 0, w-1
            while low <= high:
                middle = (low + high) // 2
                midpoint = row[middle]
                if midpoint == target:
                    return True
                elif midpoint < target:
                    low = middle + 1
                else:
                    high = middle - 1
        return False