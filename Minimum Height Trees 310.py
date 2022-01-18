from typing import List
import time


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        if len(edges) == 1:
            return [0, 1]
        incidence: dict[set] = {i: set() for i in range(n)}
        for start, end in edges:
            incidence[start].add(end)
            incidence[end].add(start)
        current: set = {i for i in range(n) if len(incidence[i]) == 1}
        visited: set = current
        while True:
            # print(current)
            # time.sleep(1)
            # check condition of end
            if len(current) == 1:
                return list(current)
            if len(current) == 2 and \
                    list(current)[1] in incidence[list(current)[0]]:
                return list(current)
            next_current = set()
            for x in current:
                candidate = (incidence[x] - visited).pop()
                if len(incidence[candidate] - visited) <= 1:
                    next_current.add(candidate)
                else:
                    next_current.add(x)
            visited.update(current)
            current = next_current


n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
assert Solution.findMinHeightTrees(None, n, edges) == [3, 4]
