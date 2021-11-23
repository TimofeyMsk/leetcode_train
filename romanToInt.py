# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        # ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000,
                'IV': 4, 'IX': 9,
                'XC': 90, 'XL': 40,
                'CD': 400, 'CM': 900}
        i = 0
        lex = []
        # print(s)
        while i != len(s):
            # print(i)
            if i + 1 == len(s):  # last symbol
                lex.append(dict[s[i]])
            elif dict[s[i+1]] > dict[s[i]]:  # double symbol
                lex.append(dict[s[i] + s[i+1]])
                i += 1  # additional right shift
            else:  # single symbol
                lex.append(dict[s[i]])
            i += 1  # regular right shift
            print(lex)
        return sum(lex)


print(Solution.romanToInt(None, "LVIII"))
