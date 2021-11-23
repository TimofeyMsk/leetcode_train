from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res: List[List[int]] = [[1], [1, 1]]
        if numRows in (1, 2):
            return res[:numRows]
        for _ in range(numRows-2):
            last_row = res[len(res)-1]
            cur = [1]
            cur += list(map(lambda x, y: x+y, last_row[:len(last_row)-1], last_row[1:]))
            cur.append(1)
            res.append(cur)
        return res


def printPascal(inp: List[List[int]]) -> None:
    width = 2+len(inp)+(len(inp)-1)*2 + 1
    for str in inp:
        # print(str)
        print(f'{str!r:^{width}}')


a = Solution.generate(None, 16)
printPascal(a)
