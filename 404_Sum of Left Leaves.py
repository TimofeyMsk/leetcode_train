# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total_sum = 0

        def go_deep(node: TreeNode, is_left: bool):
            nonlocal total_sum
            if node.left is None and node.right is None and is_left:
                total_sum += node.val
                return
            if node.left is not None:
                go_deep(node.left, is_left=True)
            if node.right is not None:
                go_deep(node.right, is_left=False)

        go_deep(root, is_left=False)
        return total_sum



t6 = TreeNode(6, None, None)
t5 = TreeNode(5, None, None)
t4 = TreeNode(4, None, None)
t3 = TreeNode(3, t6, None)
t2 = TreeNode(2, t4, t5)
t1 = TreeNode(1, t2, t3)

m3 = TreeNode(3, None, None)
m2 = TreeNode(1, None, None)
m1 = TreeNode(0, m2, None)

print(Solution.sumOfLeftLeaves(None, t1))
