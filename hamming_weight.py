def hammingWeight(self, n: int) -> int:
    return f'{n:032b}'.count('1')


print(hammingWeight(None, int('11', base=2)))
