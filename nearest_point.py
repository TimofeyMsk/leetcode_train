#  1779. Find Nearest Point That Has the Same X or Y Coordinate
# 'You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y).
# You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi).
# A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.
#
# Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
# If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.
# The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
# Example 1:
# Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
# Output: 2
# Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have
# the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index,
# so return 2.'
from typing import List


class Solution:
    def nearestValidPoint_1(self, x: int, y: int, points: List[List[int]]) -> int:
        best_point_index = -1
        best_distance = -1
        for i in range(len(points)):
            px = points[i][0]
            py = points[i][1]
            dist = abs(px - x) + abs(py - y)
            if (px == x or py == y) and (dist < best_distance or best_point_index == -1):
                best_point_index = i
                best_distance = dist

        return best_point_index
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dict = {} # key - distance, value = set of indexes
        for i, (a, b) in enumerate(points):
            d = abs(x - a) + abs(y - b)
            if x == a or y ==b:
                if d in dict:
                    dict[d].add(i)
                else:
                    dict[d] = set([i])

        print(dict)
        if dict:
            key = min(dict)
            return min(dict[key])
        else:
            return -1


print('-> ', Solution.nearestValidPoint(None, 1, 2, [[1,2], [1, 5], [4, 2]]))