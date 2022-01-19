'''The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.'''
from heapq import heappush, heappushpop
from typing import List


class MedianFinder:
    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        lst = self.lst
        if not lst or num >= lst[-1]:
            lst.append(num)
        elif num <= lst[0]:
            lst.insert(0, num)
        else:  # len(l) > 2
            l, r = 0, len(lst) - 1
            while r - l > 1:
                mid = l + (r - l) // 2
                # print(mid)
                if lst[mid] == num:
                    lst.insert(mid, num)
                    return
                if num < lst[mid]:
                    r = mid
                else:
                    l = mid
            lst.insert(r, num)

        # print(lst)

    def findMedian(self) -> float:
        lst = self.lst
        print(lst)
        if not lst:
            return
        k, r = divmod(len(lst), 2)
        if r == 1:
            return lst[k]
        else:
            return (lst[k - 1] + lst[k]) / 2


class MedianFinder1:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return self.large[0]
        mid = self.len // 2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder1()
obj.addNum(6)
print(obj.findMedian())
obj.addNum(10)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(6)
print(obj.findMedian())
obj.addNum(5)
print(obj.findMedian())
obj.addNum(0)
print(obj.findMedian())
obj.addNum(6)
print(obj.findMedian())
obj.addNum(3)  # !!!!!
print(obj.findMedian())
obj.addNum(1)
print(obj.findMedian())
obj.addNum(0)
print(obj.findMedian())
obj.addNum(0)
print(obj.findMedian())


'''["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
[[],[6],[],[10],[],[2],
[],[6],[],[5],[],[0],
[],[6],[],[3],[],[1],
[],[0],[],[0],[]]

null,6.00000,null,8.00000,null,6.00000,
null,6.00000,null,6.00000,null,5.50000,
null,6.00000,null,!!!5.50000!!!,null,5.00000,
null,4.00000,null,3.00000]'''

