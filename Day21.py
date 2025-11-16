# Day 21 - Matrix Problems
# Problems:
# 1. 74. Search a 2D Matrix
# 2. 2643. Row With Maximum Ones


class Solution74:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


class Solution2643:
    def rowAndMaximumOnes(self, mat):
        max_count = -1
        row_index = 0
        for i, row in enumerate(mat):
            count = sum(row)
            if count > max_count:
                max_count = count
                row_index = i
        return [row_index, max_count]

