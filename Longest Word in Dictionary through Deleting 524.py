'''524. Longest Word in Dictionary through Deleting
Given a string s and a string array dictionary, return the longest string
in the dictionary that can be formed by deleting some of the given string
characters. If there is more than one possible result, return the longest
word with the smallest lexicographical order. If there is no possible result,
return the empty string.
Example 1:
Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"'''

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        favorits = [w for w in dictionary
                    if Solution.is_subword(w, s)]
        if not favorits: return ''
        max_len = max([len(w) for w in favorits])
        favorits_ml = [w for w in favorits if len(w) == max_len]
        favorits_sort = sorted(favorits_ml)
        return favorits_sort[0]



    @staticmethod
    def is_subword(word: str, s: str) -> bool:
        if len(word) > len(s):
            return False
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                j += 1
            i += 1
        return True if j == len(word) else False


# print(Solution.findLongestWord(None, 'abpcplea',
#                                 ["ale", "apple", "monkey", "plea"]))
# assert Solution.findLongestWord(None, 'abpcplea',
#                                 ["ale", "apple", "monkey", "plea"]) == 'apple'

s, words = '', []
with open('524 resource.txt') as f:
    x = f.read()
    s = x[1:x.index('\"\n[')]
    words_str = x[x.index('[') + 1: x.index(']')]
    words = words_str.split(',')
words = list(map(lambda y: y[1:-1], words))
needed_output = "nbmxgkduynigvzuyblwjepn"  #  23 chars
my_notTrue_output = 'jpthiudqzzeugzwwsngebdea'  # 24 chars
print('needed_output in words', needed_output in words)
# print(s)
# print(Solution.is_subword(my_notTrue_output, s))
# print(Solution.is_subword(needed_output, s))

# print(Solution.findLongestWord(None, s,
#                                 words))
# assert Solution.findLongestWord(None, s,
#                                 words) == needed_output

