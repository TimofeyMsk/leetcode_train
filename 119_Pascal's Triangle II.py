from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur = [1]
        for i in range(rowIndex):
            cur = [1, *map(sum, zip(cur[1:], cur)), 1]
        return cur

print(Solution.getRow(None, 4))
