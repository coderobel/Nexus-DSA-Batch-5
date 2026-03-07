class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix) - 1
        columns = len(matrix[0]) - 1
        result = False
        if rows == 0:
            return True
        if columns == 0:
            return True
        for row in range(0,rows):
            for column in range(0,columns):
                if matrix[row][column] == matrix[row+1][column+1]:
                    result = True
                else:
                    return False
        return result
