# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = list()

        def go_deep(node: TreeNode, path: List[int]):
            if (node.right is None and node.left is None):
                path.append(node.val)
                paths.append(path)
                return
            if node.right is not None:
                path_copy_r = list(path)
                path_copy_r.append(node.val)
                go_deep(node.right, path_copy_r)
            if node.left is not None:
                path_copy_l = list(path)
                path_copy_l.append(node.val)
                go_deep(node.left, path_copy_l)

        go_deep(root, [])
        for p in paths:
            print(p)
        longest_path = max(len(p) for p in paths)
        multipliers = [10**i for i in range(longest_path)]
        # sum = sum(list(map(lambda x: x[0]*x[1], list(zip(multipliers, paths[0])))))
        return sum([sum(list(map(lambda x: x[0]*x[1], list(zip(multipliers, p[::-1]))))) for p in paths])


t6 = TreeNode(6, None, None)
t5 = TreeNode(5, None, None)
t4 = TreeNode(4, None, None)
t3 = TreeNode(3, t6, None)
t2 = TreeNode(2, t4, t5)
t1 = TreeNode(1, t2, t3)

m3 = TreeNode(3, None, None)
m2 = TreeNode(1, None, None)
m1 = TreeNode(0, m2, None)

print(Solution.sumNumbers(None, m1))
