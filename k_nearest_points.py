# 973. K Closest Points to Origin
# Medium
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
# return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dict = {} # key - index, value - distance
        for i, (x, y) in enumerate(points):
            dist = (x ** 2 + y ** 2) ** 0.5
            dict[i] = dist
        res = []
        print(dict)
        for i, d in sorted(dict.items(), key=lambda item: item[1]):
            print(i, d)
            if len(res) < k:
                res.append(points[i])
            else:
                break
        return res


    def kClosest_1(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda x: x[0]**2 + x[1]**2)
        return points[:k]


print(Solution.kClosest(None, [[0, 1], [1, 0]], 2))


# >>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# >>> {k: v for k, v in sorted(   x.items(), key=lambda item: item[1] )}
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}