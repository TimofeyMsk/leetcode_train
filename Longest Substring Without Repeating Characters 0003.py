class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        for i in range(len(s)):
            if s[i] in s[start: i]:
                start = s.index(s[i], start, i) + 1
            max_length = max(max_length, i - start + 1)
        return max_length

print(Solution.lengthOfLongestSubstring(None, 'abcabcd'))