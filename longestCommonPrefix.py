from functools import reduce
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        max_str_len = min([len(s) for s in strs])
        for i in range(max_str_len, 0, -1):
            prefix = reduce(lambda x, y: x if x == y else '',
                            [s[:i] for s in strs])
            if prefix != '':
                return prefix
        return ''


    def longestCommonPrefix(self, strs: List[str]) -> str:
        zarr = [i for i in zip(*strs)]
        for i, t in enumerate(zarr):
            if len(set(t)) != 1:
                return strs[0][:i]
        else:
            return strs[0][:len(zarr)]
        return None


print(Solution.longestCommonPrefix(None, ["ab", "abc"]))
