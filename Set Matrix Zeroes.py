'''Given an m x n integer matrix matrix, if an element is 0, set its entire row
and column to 0's.
You must do it in place.
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        columns = set()
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == 0:
                    rows.add(i)
                    columns.add(j)
        for i in rows:
            matrix[i] = [0]*n
        for i in set(range(m)) - rows:
            row = matrix[i]
            for j in columns:
                row[j] = 0
        # print(matrix)



matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution.setZeroes(None, matrix))
