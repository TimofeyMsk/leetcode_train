# 347. Top K Frequent Elements
# Medium
# "Given an integer array nums and an integer k, return the k most frequent elements. " \
# "You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size."
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [ch[0] for ch in c.most_common(k)]


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for n in nums:
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1

        return [k for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)][:k]


    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        duration = [releaseTimes[i] - releaseTimes[i-1] for i in range(1, len(releaseTimes))]
        duration.insert(0, releaseTimes[0])
        return max(keysPressed[i] for i, v in enumerate(duration) if v == max(duration))

    # 1287. Element Appearing More Than 25% In Sorted Array
    def findSpecialInteger(self, arr: List[int]) -> int:
        needed_len_sub = int(len(arr)*0.25)+1
        cur_int = arr[0]
        cur_count = 1
        for i in range(1,len(arr)):
            if cur_int == arr[i]:
                cur_count += 1
            else:
                cur_count = 1
                cur_int = arr[i]
            if cur_count >= needed_len_sub:
                return cur_int
        return cur_int



print(Solution.findSpecialInteger(None,[1,2,2,6,6,6,6,7,10]))
# print(Solution.slowestKey(None, [12,23,36,46,62], "spuda"))

# print(Solution.topKFrequent(None, [1, 1, 1, 2, 2, 3], 2))


