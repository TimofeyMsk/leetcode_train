from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinTreeProcessing:
    def to_array(root: TreeNode) -> List[object]:
        """
        Convert binary tree to array view.
        :root Root of tree to convert.
        :return: Array view of tree.
        """
        if root is None:
            return []
        if root.val is None:
            raise ValueError
        result = [root.val]
        last_line_nodes: List[TreeNode] = [root]
        next_line_nodes: List[TreeNode] = [root.left, root.right]
        while True:
            next_line_nodes = last_line_nodes
            last_line_nodes = []
            # check existing not None elements
            if
            for current_node in last_line_nodes:

                result.append(current_node.val)
