from typing import List
from collections import deque


def merge_sort_rec(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    k = len(nums)//2
    return merge(merge_sort_rec(nums[:k]), merge_sort_rec(nums[k:]))

def merge(a: List[int], b: List[int]) -> List[int]:
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:] if i < len(a) else b[j:])
    return res

def merge_sort_iter(nums: List[int]) -> List[int]:
    dq = deque([[x] for x in nums])
    while len(dq) > 1:
        dq.append(merge(dq.popleft(), dq.popleft()))
    return list(dq)



def is_sorted(x: List[int]) -> bool:
    for i in range(1, len(x)):
        if x[i-1] <= x[i]:
            continue
        else:
            return False
    return True


p1 = [3,2]
p2 = [3,2,1]
p3 = [3,6,5,6,4,3,9,2,1,0,4,2,7]



assert is_sorted(merge_sort_iter(p1))
assert is_sorted(merge_sort_iter(p2))
assert is_sorted(merge_sort_iter(p3))
