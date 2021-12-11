# https://leetcode.com/problems/jump-game-iii/
from typing import List, Set
import time


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        reached_indexes: Set[int] = {start}
        new_indexes: Set[int] = set()
        left_jump = start - arr[start]
        right_jump = start + arr[start]
        if right_jump < n:
            new_indexes.add(right_jump)
            reached_indexes.add(right_jump)
        if 0 <= left_jump:
            new_indexes.add(left_jump)
            reached_indexes.add(left_jump)

        while new_indexes:
            c_index = new_indexes.pop()
            if arr[c_index] == 0:
                return True
            left_jump = c_index - arr[c_index]
            right_jump = c_index + arr[c_index]
            if right_jump < n and right_jump not in reached_indexes:
                new_indexes.add(right_jump)
                reached_indexes.add(right_jump)
            if 0 <= left_jump and left_jump not in reached_indexes:
                new_indexes.add(left_jump)
                reached_indexes.add(left_jump)
        return False


class Solution2:
    def canReach(self, arr: List[int], start: int) -> bool:
        last_i = len(arr) - 1
        zero_is_reached = False
        visited_indexes: List[int] = []

        def go(c_pos: int):
            nonlocal zero_is_reached
            if zero_is_reached:
                return
            if arr[c_pos] == 0:
                zero_is_reached = True
                return
            if c_pos in visited_indexes:
                return
            visited_indexes.append(c_pos)
            jump_range = arr[c_pos]
            if c_pos + jump_range <= last_i:
                go(c_pos + jump_range)
            if 0 <= c_pos - jump_range:
                go(c_pos - jump_range)

        go(start)
        return zero_is_reached


class Solution3:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        queue = [start]

        while queue:
            pos = queue.pop(0)
            visited.add(pos)

            if arr[pos] == 0:
                return True

            p = pos + arr[pos]
            if 0 <= p < n and p not in visited:
                queue.append(p)
            p = pos - arr[pos]
            if 0 <= p < n and p not in visited:
                queue.append(p)

        return False


assert Solution.canReach(None, [4, 2, 3, 0, 3, 1, 2], 5) is True
assert Solution.canReach(None, [3, 0, 2, 1, 2], 2) is False
start_time = time.perf_counter()
assert Solution3.canReach(None,
                          [1] * 50000 + [0],
                          2) is True
print(f'Solution3 elapsed in: {time.perf_counter() - start_time} seconds.')
assert Solution.canReach(None, [3, 0, 2, 1, 2], 2) is False
start_time = time.perf_counter()
assert Solution.canReach(None,
                         [1] * 50000 + [0],
                         2) is True
print(f'Solution elapsed in: {time.perf_counter() - start_time:.3f} seconds.')

# Solution elapsed in: 13.772 seconds.
# Solution elapsed in: 13.787 seconds.


l = [x for x in range(10 ** 5)]
start_time = time.perf_counter()
print(99999 in l)
print(
    f'Search in list elapsed in: {time.perf_counter() - start_time:.6f} seconds.')
s = set(l)
start_time = time.perf_counter()
print(99999 in s)
print(
    f'Search in set elapsed in: {time.perf_counter() - start_time:.6f} seconds.')

l = list()
start_time = time.perf_counter()
for x in range(10 ** 7):
    l.append(x)
print(
    f'Filling list elapsed in: {time.perf_counter() - start_time:.6f} seconds.')

s = set()
start_time = time.perf_counter()
for x in range(10 ** 7):
    s.add(x)
print(
    f'Filling set elapsed in: {time.perf_counter() - start_time:.6f} seconds.')

d = dict()
start_time = time.perf_counter()
for x in range(10 ** 7):
    d[x] = 1
print(
    f'Filling dict elapsed in: {time.perf_counter() - start_time:.6f} seconds.')



