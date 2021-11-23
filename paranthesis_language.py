class Solution:
    def isValid(self, s: str) -> bool:
        open_parethesis = ['(', '[', '{']
        close_parenthesis = [')', ']', '}']
        corresponding = dict(zip(open_parethesis, close_parenthesis))
        history = {}
        deep = 0  # current deep of tree
        for sym in s:
            if sym in open_parethesis:
                history[deep] = sym
                deep += 1
            elif sym in close_parenthesis:
                if sym == corresponding.get(history.get(deep - 1)):
                    deep -= 1
                else:
                    return False

            if deep < 0:
                return False

        if deep != 0:
            return False
        else:
            return True
