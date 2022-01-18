class MinStack:

    def __init__(self):
        self.stack = []
        self.sorted_stack = []  # ascending

    def push(self, val: int) -> None:
        self.stack.append(val)
        ss = self.sorted_stack
        if not ss or val >= ss[-1]:
            ss.append(val)
            print(ss, self.stack)
            return
        if val <= ss[0]:
            ss.insert(0, val)
        else:
            for i in range(1, len(ss)):
                if ss[i - 1] <= val <= ss[i]:
                    ss.insert(i, val)
                    break
        print(ss, self.stack)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            self.sorted_stack.remove(val)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        return self.sorted_stack[0]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)
print('--> ', obj.sorted_stack, obj.stack)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
obj.pop()
obj.pop()
print('--> ', obj.sorted_stack, obj.stack)


'''
["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
'''
