from BinaryTree import BinaryTree, TreeNode
from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        is_balanced = True

        def go(node: TreeNode) -> int:
            """Return height of tree."""
            nonlocal is_balanced
            if not is_balanced:
                return 0
            height_left_subtree = 0
            height_right_subtree = 0
            if not node.left and not node.right:
                return 1
            if node.left:
                height_left_subtree = go(node.left)
            if node.right:
                height_right_subtree = go(node.right)
            if abs(height_left_subtree - height_right_subtree) > 1:
                is_balanced = False
            return max(height_left_subtree, height_right_subtree) + 1

        go(root)
        return is_balanced
