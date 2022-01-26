from typing import List
from random import randint
from statistics import median


def find_median(nums: List[int]) -> float:
    if len(nums) & 1:  # odd len
        return find_kth_element_bisect(nums, len(nums)//2 + 1)
    else:
        half = len(nums)//2
        a = find_kth_element_bisect(nums, half)
    left, equal, right = [], [], []
    for x in nums:
        if x < a:
            left.append(x)
        elif x == a:
            equal.append(x)
        elif x > a:
            right.append(x)
    l_len, e_len, r_len = len(left), len(equal), len(right)
    if e_len == 1:
        b = min(right)
    else:
        if half == l_len + e_len:
            b = min(right)
        else:
            b = a
    return (a + b)/2


def find_kth_element_bisect(nums: List[int], k: int) -> int:
    """Return k-th by ascending element in nums."""
    n = len(nums)
    if k > n:
        raise ValueError(f"Length if nums ={n} more then parameter k = {k}.")
    if k == 0:
        return min(nums)
    elif k == n:
        return max(nums)
    edge = nums[randint(0, n-1)]
    left, equal, right = [], [], []
    for x in nums:
        if x < edge:
            left.append(x)
        elif x == edge:
            equal.append(x)
        elif x > edge:
            right.append(x)
    l_len, e_len, r_len = len(left), len(equal), len(right)
    if k <= l_len:
        return find_kth_element_bisect(left, k)
    elif k > l_len + e_len:
        return find_kth_element_bisect(right, k - l_len - e_len)
    elif l_len < k <= l_len + e_len:
        return edge


def find_kth_element_by_sort(nums: List[int], k: int) -> int:
    if k > len(nums):
        raise ValueError(f"Length if nums ={len(nums)} more then parameter k ="
                         f" {k}.")
    return sorted(nums)[k-1]


k, nums = 4, [1,4,3,6,8,4,3,22,5,6,7,5,3,354,7,5,4,34,5,6,7,0,0,8,67,5,6,534,
              1000, 1001, 1002, 1003] + list(range(1004, 1030))
# print(find_kth_element_bisect(nums, k))
# print(find_kth_element_by_sort(nums, k))
print("nums is ", sorted(nums))
for i in range(1, len(nums)):
    print("k = ", i)
    assert find_kth_element_bisect(nums, i) == find_kth_element_by_sort(nums, i)
print("End of compare test of find_kth_element_bisect and "
      "find_kth_element_by_sort")
print("="*80)

print("Compare test if my median function and in built-in median.")
for m in range(1, len(nums)):
    print("m = ", m)
    print(median(nums[:m]))
    assert find_median(nums[:m]) == median(nums[:m])
print("End of compare test if my median function and in built-in median.")
