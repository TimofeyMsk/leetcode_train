from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        c = 0
        while True:
            if c == len(nums) - 1:
                break
            if nums[c] == nums[c+1]:
                nums.pop(c+1)
            else:
                c += 1

class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp=1
        for i in range(1,len(nums)):
            if nums[temp-1]!=nums[i]:
                nums[temp]=nums[i]
                temp+=1
        return temp


nums = [1,2,2,3,3,3,4]
Solution1.removeDuplicates(None, nums)
print(nums)
