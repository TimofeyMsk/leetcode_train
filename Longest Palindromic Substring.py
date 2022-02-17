"""Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
"""
from timeit import default_timer
from random import choices

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        max_length = 0
        longest_palindrome = ''
        for i in range(n):
            for j in range(i + 1, n + 1):
                if s[i: j] == ''.join(reversed(s[i: j])):
                    if j - i > max_length:
                        max_length = j - i
                        longest_palindrome = s[i: j]
        return longest_palindrome

    def longestPalindrome_1(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        if n == 2:
            return s if s[0] == s[1] else s[0]
        pairs = [i for i in range(n - 1) if s[i] == s[i + 1]]
        triplets = [i for i in range(n - 2) if s[i] == s[i + 2]]
        len_max = 1
        palindrome_max = s[0]

        def grow_palindrome(i: int, j: int):
            nonlocal palindrome_max, len_max
            while i >= 0 and j < n and s[i] == s[j]:
                if j - i + 1 > len_max:
                    palindrome_max = s[i: j + 1]
                    len_max = j - i + 1
                i -= 1
                j += 1

        for i in pairs:
            grow_palindrome(i, i + 1)
        for i in triplets:
            grow_palindrome(i, i + 2)
        return palindrome_max

    def longestPalindrome_3(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]:
            return s
        else:
            maxlen = 0
            start = 0
            for i in range(1, len(s)):
                odd = s[i - maxlen - 1: i + 1]
                even = s[i - maxlen:i + 1]
                if i - maxlen - 1 >= 0 and odd == odd[::-1]:
                    start = i - maxlen - 1
                    maxlen += 2
                    continue
                if even == even[::-1]:
                    start = i - maxlen
                    maxlen += 1
        return s[start:start + maxlen]

    def longestPalindrome_4(self, s: str) -> str:  # sliding window
        n = len(s)
        if n == 1:
            return s
        if n == 2:
            return s if s[0] == s[1] else s[0]
        len_max = 1
        long_polind_end = 0
        for end in range(1, n):
            first = s[end - len_max: end + 1]  # len = len_max + 1
            second = s[end - len_max - 1: end + 1]  # len = len_max + 2
            if first == first[::-1]:
                long_polind_end = end
                len_max += 1
            if end - len_max - 1 >= 0 and second == second[::-1]:
                long_polind_end = end
                len_max += 1 if first == first[::-1] else 2
        return s[long_polind_end - len_max + 1: long_polind_end + 1]


# print('Ans: ', Solution.longestPalindrome_3(None, 'aaaa'))
s1 = "zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"
s2 = choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10000)
s = s2
print(f'------REPORT [len(s)={len(s)}] ------')
t0 = default_timer()
print('Ans: ', Solution.longestPalindrome(None, s))
t1 = default_timer()
print(f'Bruteforce algorithm: {t1 - t0:.6f}')
print('Ans: ', Solution.longestPalindrome_1(None, s))
t2 = default_timer()
print(f'Polindrome growing algorithm: {t2 - t1:.6f}')
print(f'Second faster then first in {(t1 - t0) / (t2 - t1):.4f} times.')
print('Ans: ', Solution.longestPalindrome_3(None, s))
t3 = default_timer()
print(f'odd_even algorithm: {t3 - t2:.6f}')
print(f'Third faster then first in {(t1 - t0) / (t3 - t2):.4f} times.')
print('Ans: ', Solution.longestPalindrome_4(None, s))
t4 = default_timer()
print(f'Sliding window algorithm: {t4 - t3:.6f}')
print(f'Forth faster then first in {(t1 - t0) / (t4 - t3):.4f} times.')
# print('Ans: ', Solution.longestPalindrome(None, "a"))
# print('Ans: ', Solution.longestPalindrome(None, "bb"))
# print(Solution.longestPalindrome(None, "babad"))

"""------REPORT [len(s)=10000] ------
Ans:  
Bruteforce algorithm: 1777.467192
Ans:  ['s', '3', 'w', '3', 's']
Polindrom growing algorithm: 0.001640
Second faster then first in 1084085.8691 times.
Ans:  ['s', '3', 'w', '3', 's']
odd_even algorithm: 0.005911
Third faster then first in 300725.3396 times.
Ans:  ['s', '3', 'w', '3', 's']
Sliding window algorithm: 0.005879
Forth faster then first in 302367.4733 times."""