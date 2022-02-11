'''Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]'''
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a3 = ['Fizz' if i % 3 == 0 else '' for i in range(n + 1)]
        a5 = ['Buzz' if i % 5 == 0 else '' for i in range(n + 1)]
        return [a3[i]+a5[i] if a3[i] or a5[i] else str(i) for i in range(n+1)][1:]
        # return list(map(lambda x, y: x + y, a3, a5))


print(Solution.fizzBuzz(None, 15))
