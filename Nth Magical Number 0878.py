import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # Let a > b
        if a < b:
            a, b = b, a
        nok = math.lcm(a, b)
        items_in_nok = nok // a + nok // b - 1  # count of items between 0 and nok
        nok_count, relative_index = divmod(n, items_in_nok)
        if relative_index == 0:
            return (nok * nok_count) % (10 ** 9 + 7)
        a_arr = [a * i for i in range(1, nok // a)]
        b_arr = [b * i for i in range(1, nok // b)]
        c_arr = sorted(a_arr + b_arr)
        return (nok * nok_count + c_arr[relative_index - 1]) % (10 ** 9 + 7)


assert Solution.nthMagicalNumber(None, 1, 2, 3) == 2
assert Solution.nthMagicalNumber(None, 4, 2, 3) == 6
assert Solution.nthMagicalNumber(None, 5, 2, 4) == 10
assert Solution.nthMagicalNumber(None, 7, 5, 8) == 24
assert Solution.nthMagicalNumber(None, 1000000000, 40000, 40000) \
       == 999720007

# k = a // b
# nok = math.lcm(a, b)
# g, f = divmod(n, k + 1)
# if f == 0:
#     return a * g
# else:
#     return b * (g * k + g // (nok // a) + f)
