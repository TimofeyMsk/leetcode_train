from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = c_len = 0
        if k == 0:
            for x in nums:
                if x == 1:
                    c_len += 1
                else:
                    c_len = 0
                max_len = max(max_len, c_len)
            return max_len
        start = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                if k > 0:
                    k -= 1
                else:
                    start = nums.index(0, start, i) + 1
            c_len = i - start + 1
            max_len = max(max_len, c_len)
        return max_len

    def longestOnes2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        res = 0

        for right in range(n):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            print(nums[left: right+1])
            # res = max(res, right - left + 1)

        return right - left + 1


print(Solution.longestOnes2(None, [1,1,1,0,0,0,1,1,1,1,0], k = 2))
assert Solution.longestOnes2(None, [1,1,1,0,0,0,1,1,1,1,0], k = 2) == 6
assert Solution.longestOnes2(None, [0]*10+[1]+[0]*10, k = 2) == 3
assert Solution.longestOnes2(None, [0,0,1,1,1,0,0],k = 0) == 3




# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.