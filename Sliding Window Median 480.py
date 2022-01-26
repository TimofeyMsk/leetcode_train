from typing import List
from bisect import bisect_left, insort


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        def get_median(x: List[int]) -> float:
            m = len(x)
            if m & 1:
                return x[m // 2]
            else:
                return (x[m // 2 - 1] + x[m // 2]) / 2

        output = []
        window = sorted(nums[:k])
        output.append(get_median(window))
        for first_item, new_item in zip(nums[:-k], nums[k:]):
            window.pop(bisect_left(window, first_item))
            insort(window, new_item)
            output.append(get_median(window))
        return output


assert Solution.medianSlidingWindow(None, [1, 3, -1, -3, 5, 3, 6, 7], k=3) == [
    1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]
