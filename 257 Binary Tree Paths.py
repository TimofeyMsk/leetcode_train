# Definition for a binary tree node.
from typing import Optional, List
from BinaryTree import BinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        result = []

        def go(node: TreeNode, current_path: List[object]) -> None:
            if node.left is None and node.right is None:
                current_path.append(node.val)
                nonlocal result
                result.append("->".join([str(x) for x in current_path]))
                return
            if node.left is not None:
                go(node.left, current_path.copy() + [node.val])
            if node.right is not None:
                go(node.right, current_path.copy() + [node.val])

        go(root, [])
        return result


bt_root = BinaryTree([1, 2, 3, None, 5]).get_root()
print(Solution.binaryTreePaths(None, bt_root))
