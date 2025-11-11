# Day 8 - #100DaysOfInterviewCodingChallenge
# Topic: Matrix Problems
# Problems: 240. Search a 2D Matrix II | 48. Rotate Image | 54. Spiral Matrix

# -----------------------------------------------------------
# 240. Search a 2D Matrix II
# -----------------------------------------------------------
class Solution1:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

# -----------------------------------------------------------
# 48. Rotate Image
# -----------------------------------------------------------
class Solution2:
    def rotate(self, matrix):
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for row in matrix:
            row.reverse()
        return matrix

# -----------------------------------------------------------
# 54. Spiral Matrix
# -----------------------------------------------------------
class Solution3:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res

