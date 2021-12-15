class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int('0b'+ a)
        b = int('0b'+ b)
        return f'{a+b:b}'


