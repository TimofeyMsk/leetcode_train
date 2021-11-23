
from typing import List
from typing import Tuple
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(opened: int, closed: int, current: str):
            if opened + closed == 0:
                res.append(current)
                return
            if opened > 0:
                generate(opened - 1, closed, current + '(')
            if opened < closed:
                generate(opened, closed - 1, current + ')')
        generate(n, n, '')
        return res


def get_all_permutation(elements: List) -> List[Tuple]:
    n = len(elements)
    res = []

    def generate(left_elements: List, current_permutation: List):
        if len(left_elements) == 0:
            res.append(tuple(current_permutation))
            return
        for j in range(len(left_elements)):
            x = left_elements.pop(j)
            current_permutation.append(x)
            generate(left_elements, current_permutation)
            left_elements.insert(j, x)
            current_permutation.pop()

    generate(elements, [])
    return res


print(get_all_permutation(list('1234')))
