# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
# Constraints:
# 1 <= n <= 2**31 - 1
# 1 <= pick <= n
import random


class Solution:
    def guess(num: int) -> int:
        # return random.randint(-1, 1)
        a = 2147483647
        if num == a:
            return 0
        elif num > a:
            return -1
        elif num < a:
            return 1

    def guessNumber(self, n: int) -> int:
        l = 1
        r = 2**31 - 1
        if Solution.guess(r) == 0:
            return r
        while 1:
            g = (r - l) // 2 + l
            print(l, g, r)
            flag = Solution.guess(g)
            # print(flag)
            if flag == 0:
                return g
            elif flag == 1:  # turn right
                l = g
                continue
            elif flag == -1:  # turn left
                r = g
                continue

    def isPalindrome(self, x: int) -> bool:
        rev = ''.join([i for i in reversed(str(y))])
        if str(x) == rev:
            return True
        else:
            return False


print(Solution.guessNumber(None, 100))



