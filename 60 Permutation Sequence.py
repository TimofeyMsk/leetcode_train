from typing import List
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutation: List[int] = []
        source = [i for i in range(1, n+1)]
        k -= 1

        while source:
            block_len = math.factorial(len(source) - 1)
            block_ind = k // block_len
            permutation.append(source[block_ind])
            del source[block_ind]
            k = k % block_len
        return ''.join([str(x) for x in permutation])


f = lambda x, y: Solution.getPermutation(None, x, y)
for m in range(1, math.factorial(3) + 1):
    print(f(3, m))



