class Solution:
    def climbStairs(self, n: int) -> int:
        # return n if n in (0, 1, 2) else Solution.climbStairs(None, n-2) + Solution.climbStairs(None, n-1)
        if n in (0, 1, 2):
            return n
        f_n_2 = 1  # f(n-2)
        f_n_1 = 2  # f(n-1)
        for _ in range(n-2):
            f_n = f_n_2 + f_n_1
            f_n_2 = f_n_1  # shift variables
            f_n_1 = f_n  # shift variables
        return f_n_1

    def climbStairs(self, n: int) -> int:
        # return n if n in (0, 1, 2) else Solution.climbStairs(None, n-2) + Solution.climbStairs(None, n-1)
        if n in (0, 1, 2):
            return n
        a = 1  # f(n-2)
        b = 2  # f(n-1)
        for _ in range(n-2):
            a, b = b, a + b
        return b

print(Solution.climbStairs(None, 3))