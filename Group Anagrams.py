'''Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the
answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different
 word or phrase, typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
from typing import List
from functools import reduce

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if not strs or strs
        groups: dict = {}
        for s in strs:
            letters = ''.join(sorted(s)) if s else s
            group = groups.setdefault(letters, [])
            group.append(s)

        return list(groups.values())


strs_1 = ["eat","tea","tan","ate","nat","bat"]
strs_2 = ['']
print(Solution.groupAnagrams(None, strs_2))