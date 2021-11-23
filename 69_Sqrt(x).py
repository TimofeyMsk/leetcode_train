class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0, 1):
            return x
        current = 0
        for i in range(1, x):
            if i**2 > x:
                return current
            else:
                current = i

print(Solution.mySqrt(None, 41231233))