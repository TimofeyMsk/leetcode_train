a = "in file"


class A:
    a = "in class"

    def __init__(self):
        self.a = "in init"
    def fun():
        a = "in function"

        def met():
            nonlocal a
            a = "in method"
        met()
        return a

    print(fun())


inst = A()
print(a, A.a, inst.a)
