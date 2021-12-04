from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def go(source: List[int], workpiece: List[int]):
            if not source:
                permutations.append(workpiece)
            for x in source:
                new_source = source.copy()
                new_source.remove(x)
                new_workpiece = workpiece.copy()
                new_workpiece.append(x)
                go(new_source, new_workpiece)

        go(nums, [])
        return permutations


f = lambda x: Solution.permute(None, x)
