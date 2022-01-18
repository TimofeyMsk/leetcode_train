# Given a signed 32-bit integer x, return x with its digits reversed. If reversing
# x causes the value to go outside the signed 32-bit integer range
# [-2**31, 2**31 - 1] , then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or
#                                                                     unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = s[::-1]

        if s[-1] == '-':
            del s[-1]
            is_neg = True
        else:
            is_neg = False
        s = ''.join(['0'] * (10 - len(s))) + s
        if not is_neg:
            if s < str(2 ** 31 - 1):
                return str(int(s))
            else:
                return 0
        else:
            if s < str(2 ** 31):
                return '-' + str(int(s))
            else:
                 return 0

    def reverse2(self, x: int) -> int:
        is_neg = False
        if x < 0:
            is_neg = True
        s = str(x)
        rs_iterator = reversed(s[1:] if is_neg else s)
        rs = ''.join(rs_iterator)
        max_int_abs_str = str(2 ** 31 - 1)  # 10 symbols
        min_int_abs_str = str(2 ** 31)  # 10 symbols
        # Add zeros to beginning of rs till 10 symbols. For string compare.
        rs = ''.join('0' for i in range(10 - len(rs))) + rs
        if is_neg:
            if rs > min_int_abs_str:
                return 0
            else:
                return int('-' + rs)
        else:
            if rs > max_int_abs_str:
                return 0
            else:
                return int(rs)


