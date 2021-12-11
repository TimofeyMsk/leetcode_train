from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target_node = len(graph) - 1
        pathes: List[List[int]] = []

        def go(current_node: int = 0, visited: List[int] = [0]):
            if current_node == target_node:
                pathes.append(visited)
            for next in graph[current_node]:
                go(next, visited=visited + [next])

        go()
        return pathes


graph1 = [[4, 3, 1], [3, 2, 4], [3], [4], []]
print(Solution.allPathsSourceTarget(None, graph1))
assert Solution.allPathsSourceTarget(None, graph1) == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
