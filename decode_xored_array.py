from typing import List


def decode(self, encoded: List[int], first: int) -> List[int]:
    res = []
    previous = first
    for e in encoded:
        x = e ^ previous
        res.append(x)
        previous = x
    return res



# a XOR b = a&~b|~a&b
# (a^b)^b=a
# a^x=b <=>
# x^a=b
# x^a^a=b^a
# x=b^a
