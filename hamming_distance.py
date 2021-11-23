from typing import List


def hammingDistance(self, x: int, y: int) -> int:
    print(f'{x:b}\n{y:b}')
    return f'{x^y:b}'.count('1')


# print(hammingDistance(None, int(0b1111), int(0b10001111)))


def total_hammingDistance(self, nums: List[int]) -> int:
    s_nums = [f'{x:032b}' for x in nums]
    # for n in nums: print(f'{n:04b}')
    res = 0
    for i in range(32):
        ones = 0
        for s in s_nums:
            ones += 1 if s[i] == '1' else 0
        # print(f'Registr {i}, ones: {ones}' )
        res += ones * (len(s_nums) - ones)
    return res


print(total_hammingDistance(None, [4, 14, 2]))
