from typing import List, Set


class TreeNode:
    def __init__(self, value: str = 'Start'):
        self.value: str = value
        self.children: Set[TreeNode] = set()
        self.is_leaf = False

    def create_child(self, child_value: str):
        """Create child with value child_value for this node and return child
        node. If child with child_value already exists, return him."""
        existing_child: TreeNode = self.get_child(child_value)
        if existing_child:
            return existing_child
        new_child: TreeNode = TreeNode(child_value)
        self.children.add(new_child)
        return new_child

    def get_child(self, value: str):
        """Return child of this node if exists, else return None."""
        for x in self.children:
            if x.value == value:
                return x
        return None


class StreamChecker:

    def __init__(self, words: List[str]):
        self.chars = ''
        self.root = TreeNode()
        """Root of suffix tree for words."""

        for word in words:
            c_node = self.root
            for x in word[::-1]:
                c_node = c_node.create_child(x)
            c_node.is_leaf = True

    def query(self, letter: str):
        self.chars += letter
        c_node = self.root
        for char in self.chars[::-1]:
            c_node = c_node.get_child(char)
            if not c_node:
                return False
            if c_node.is_leaf:
                return True

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
