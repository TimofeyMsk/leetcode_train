# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def go(root: TreeNode):
            if root is None:
                return
            root.left, root.right = root.right, root.left
            go(root.left)
            go(root.right)
        go(root)
        return root