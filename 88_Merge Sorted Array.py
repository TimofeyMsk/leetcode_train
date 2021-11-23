from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for _ in range(n):
            nums1.pop()
        if len(nums1) == 0:
            for x in nums2:
                nums1.append(x)
            return
        if len(nums2) == 0:
            return
        i, j = 0, 0
        while not (j >= n):
            if nums1[i] >= nums2[j]:  # insert left
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                continue
            if nums1[i] < nums2[j]:  # insert right
                if i != len(nums1)-1:  # if not last element in nums1
                    if nums1[i+1] < nums2[j]:
                        i += 1
                        continue
                nums1.insert(i+1, nums2[j])
                i = i+2 if i+2 < len(nums1) else len(nums1) - 1
                j += 1


a =[1,2,3,0,0,0]
b =[2,5,6]
Solution.merge(None,a,3,b,3)
print(a)