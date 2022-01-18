'''Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node) -> (bool, int, int):
            if not node.left and not node.right:
                return (True, node.val, node.val)
            l_min, l_max, l_bool, r_min, r_max, r_bool = \
                float('inf'), float('-inf'), 1, float('inf'), float('-inf'), 1
            if node.left:
                l_bool, l_min, l_max = helper(node.left)
            if node.right:
                r_bool, r_min, r_max = helper(node.right)
            return (l_bool and r_bool and l_max < node.val and r_min > node.val,
                    min(l_min, r_min, node.val),
                    max(l_max, r_max, node.val))

        return helper(root)[0]
