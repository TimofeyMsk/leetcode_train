from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        lst = [*s]
        pars = {'(': ')', '[': ']', '{': '}'}

        def dive(l: List[str], level: int) -> str:
            current = l[0]
            next = l[1]
            if current in pars.keys():
                if next == pars[current]:  # correct closing
                    l.pop(0)
                    l.pop(0)






print(Solution.isValid(None, '([][{}])'))