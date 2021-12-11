from typing import Optional
from BinaryTree import BinaryTree, TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maximum = 0
        if not root:
            return 0
        def go(next_node: TreeNode, cur_depth: int):
            if not next_node.left and not next_node.right:
                cur_depth += 1
                nonlocal maximum
                maximum = max(maximum, cur_depth)
            if next_node.left:
                go(next_node.left, cur_depth + 1)
            if next_node.right:
                go(next_node.right, cur_depth + 1)

        go(root, 0)
        return maximum


tree_array = [3, 9, 20, None, None, 15, 7]
root_1 = BinaryTree(tree_array).get_root()
print(Solution.maxDepth(None, root_1))

tree_array = []
root_1 = BinaryTree(tree_array).get_root()
print(Solution.maxDepth(None, root_1))
