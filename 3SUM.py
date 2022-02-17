'''Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]'''
from typing import List
from timeit import default_timer
from random import sample

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets: set = set()
        for i, x in enumerate(nums):
            j, k = i + 1, n - 1
            while j < k:
                summa = x + nums[j] + nums[k]
                if summa == 0:
                    triplets.add((x, nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif summa > 0:
                    k -= 1
                elif summa < 0:
                    j += 1
        return [list(x) for x in triplets]

    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        t0_ = default_timer()
        n = len(nums)
        pairs_sum: dict = {}
        triplets: set = set()
        for j in range(n):
            for k in range(j + 1, n):
                pairs_sum.setdefault(0 - nums[j] - nums[k], []).append((j, k))
        t1_ = default_timer()
        print(f'Pairs_sum calculated in {t1_-t0_:.3}')
        for i in range(n):
            if nums[i] in pairs_sum:
                pairs = pairs_sum[nums[i]]
                for pair in pairs:
                    if i in pair:
                        continue
                    triplet = tuple(sorted(
                        [nums[i], nums[pair[0]], nums[pair[1]]]))
                    triplets.add(triplet)
        res = [list(x) for x in triplets]
        t2_ = default_timer()
        print(f'Triple generation calculated in {t2_-t1_:.3}')
        return res




nums_1 = [-4, -1, -1, 0, 1, 2]
n = int(input())
nums_2 = sample(range(-100000, 100000), n)

# print(Solution.threeSum(None, nums_1))  # [[-1, -1, 2], [-1, 0, 1], [-1, 0, 1]]
# print(Solution.threeSum_2(None, nums_1))  # [[-1, -1, 2], [-1, 0, 1], [-1, 0,
# 1]]
# assert Solution.threeSum(None, nums) == [[-1,0,1], [-1,-1,2]]

t0 = default_timer()
a = Solution.threeSum(None, nums_2)
print('Sorted calculated.')
t1 = default_timer()
b = Solution.threeSum_2(None, nums_2)
t2 = default_timer()
print(f'------REPORT (n = {n})------')
print(f'len(a)  = {len(a)} ?? {len(b)} = len(b).')
print(f'size(a) = {a.__sizeof__()/1000}KB ?? {b.__sizeof__()/1000}KB = size('
      f'b).')
print(f'On sorted nums: {t1-t0:.3f}')
print(f'On hashed nums: {t2-t1:.3f}')
print(f'First time is {(t1-t0)/(t2-t1):.3f} percent from second time.')
'''------REPORT (n = 4 000)------
len(a)  = 40226 ?? 40226 = len(b)
On sorted nums: 1.1921835999237373
On hashed nums: 5.704196500009857
First time is 0.20900114502045594 percent from second time.
------REPORT (n = 10 000)------
len(a)  = 633909 ?? 633909 = len(b)
On sorted nums: 7.996233899961226
On hashed nums: 38.99067750002723
First time is 0.20508066062600838 percent from second time.'''