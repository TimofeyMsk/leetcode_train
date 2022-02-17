'''Given an integer n, return the number of prime numbers that are strictly less than n.
Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.'''
from typing import List
from timeit import default_timer


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        numbers: List[int] = [None, None] + [0 for i in range(2, n + 1)]
        p = 2
        while p <= n ** 0.5 // 1 + 1:
            numbers[p ** 2:n:p] = [1 for i in range(p ** 2, n, p)]
            p = numbers.index(0, p + 1)
        return numbers.count(0) - 1

    def countPrimes_2(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [1] * (n // 2)
        for i in range(3, int(n ** .5) + 1, 2):
            if primes[i // 2]:
                primes[i * i // 2::i] = [0] * (
                            (n - i * i - 1) // (2 * i) + 1)
        return sum(primes)

t1 = default_timer()
for i in range(10000):
    print(f'{i} - ', Solution.countPrimes_2(None, i))
print(f'Elapsed {default_timer() - t1} seconds.')

# Elapsed 6.750897100020666 seconds. - countPrimes
# Elapsed 4.518675300001632 seconds. - countPrimes
# Elapsed 4.501118999964092 seconds. - countPrimes
# Elapsed 0.686943800013978 seconds. - countPrimes_2
