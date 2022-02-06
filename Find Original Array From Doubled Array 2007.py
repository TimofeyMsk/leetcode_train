'''An integer array original is transformed into a doubled array changed by
 appending twice the value of every element in original, and then randomly
 shuffling the resulting array.
Given an array changed, return original if changed is a doubled array. If
changed is not a doubled array, return an empty array. The elements in original
 may be returned in any order.
Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].'''
from typing import List
from bisect import bisect_left
from timeit import default_timer
from collections import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n & 1:
            return []
        t1 = default_timer()
        changed.sort()
        original = []
        t2 = default_timer()
        print('Sorting time:', t2-t1)

        def extract(value: [int]) -> [int | None]:
            index = bisect_left(changed, value)
            if index < len(changed) and changed[index] == value:
                return changed.pop(index)
            else:
                return None

        while changed:
            x = changed.pop(0)
            if extract(x * 2) is not None:
                original.append(x)
            else:
                return []
        print('Get original time:', default_timer() - t2)
        return original

    def findOriginalArray_hashmap(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n & 1:
            return []
        t1 = default_timer()
        original = []
        zero_count = changed.count(0)
        if zero_count > 0:
            if not zero_count & 1: # even
                changed = [y for y in changed if y !=0]
                original = [0]*(zero_count//2)
            else:
                return []
        changed.sort()
        count = dict(Counter(changed))
        t2 = default_timer()
        print('Create count and sort:', t2 - t1)

        for x in changed:
            if x not in count or count[x] == 0:
                continue
            if x*2 in count and count[x*2] > 0:
                original.append(x)
                count[x] -= 1
                count[x*2] -= 1
        print('Get original time:', default_timer() - t2)
        if not any(count.values()):
            return original
        else:
            return []


class Solution1:
    def findOriginalArray(self, changed: List[int]) -> List[int]:


# print(Solution.findOriginalArray(None, [1,3,4,2,6,8]))
# assert Solution.findOriginalArray(None, [1,3,4,2,6,8]) == [1,3,4]
assert Solution.findOriginalArray(None, [0,0,0,0]) == [0,0]
# assert Solution.findOriginalArray(None, [3, 3, 3, 3]) == []
#
# with open('2007 resource.txt') as f:
#     x = f.read()[1:-1].split(',')
#     x = list(map(int, x))
#     f.close()
#
# # print(len(x), x[1: 15])
# assert Solution.findOriginalArray(None, x) == []

# with open('2007 resource 2.txt') as f:
#     x = f.read()[1:-1].split(',')
#     x = list(map(int, x))
#     f.close()
#
# # print(len(x), x[1: 15])
# # print(Solution.findOriginalArray(None, x))
# Solution.findOriginalArray_hashmap(None, x)

# bisect
# Sorting time: 0.015144699995289557
# Get original time: 0.8426805000053719
# hashmap
# Create count and sort: 0.028047200001310557
# Get original time: 0.03817279999202583


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        if counter[0] % 2:
            return []

        for c in sorted(counter):
            if counter[c] > counter[c * 2]:
                return []
            if c:
                counter[c * 2] -= counter[c]
            else:
                counter[c] //= 2

        return list(counter.elements())

