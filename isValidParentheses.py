

class Solution:
    def isValid(self, s: str) -> bool:
        opened = '([{'
        closed = ')]}'
        stack = []
        for x in s:
            if x in opened:
                stack.append(closed[opened.index(x)])
            elif x in closed and stack:
                if x != stack.pop():
                    return False
            else:
                return False
        return not stack



print(Solution.isValid(None, '([][{}]))'))