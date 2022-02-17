'''Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
Example 1:
Input: n = 27
Output: true'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
        # 1162261467 = 3**[log(MaxInt, 3) // 1] = 3**19
        # MaxInt == 2**31 - 1

for i in range(1, 100000):
    if Solution.isPowerOfThree(None, i):
        print(i)