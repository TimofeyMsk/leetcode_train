'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Accepted
1,782,652
Submissions
3,643,397
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cur_sum = max_sum = nums[0]

        for x in nums[1:]:
            cur_sum = max(x, cur_sum + x)
            max_sum = max(cur_sum, max_sum)
        return max_sum
