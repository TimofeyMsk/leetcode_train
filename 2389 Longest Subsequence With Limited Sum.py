"""
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that 
you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
"""

from bisect import bisect_right, bisect_left
from itertools import accumulate
from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        answers = []
        print(nums)
        for q in queries:
            if q < nums[0]:
                answers.append(0)
                continue
            if q == nums[0]:
                answers.append(1)
                continue
            if q > nums[-1]:
                answers.append(len(nums))
                continue

            s, e = 0, len(nums)
            while(e-s>1):
                print(s, e)
                if q < (summ := nums[(mid := s + (e - s) // 2)]):
                    e = mid
                elif q > summ:
                    s = mid
                elif q == summ:
                    s, e = mid, mid + 1
            answers.append(s+1)
        return answers

    
nums = [4,5,2,1]
queries = list(range(14))
print(nums, queries)
print(Solution.answerQueries(None, nums, queries=queries))


class Solution_1:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = list(accumulate(sorted(nums)))
        return [bisect_right(nums, q) for q in queries]





