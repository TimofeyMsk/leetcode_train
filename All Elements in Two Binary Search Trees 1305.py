'''1305. All Elements in Two Binary Search Trees (Medium)
Share
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.
Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3] Output: [0,1,1,2,3,4]
Example 2:
Input: root1 = [1,null,8], root2 = [8,1] Output: [1,1,8,8]'''


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result: List[int] = []
        a = Solution.traverse_inorder(root1)
        b = Solution.traverse_inorder(root2)
        while a and b:
            if a[0] <= b[0]:
                result.append(a.pop(0))
            else:
                result.append(b.pop(0))
        if a:
            result.extend(a)
        else:
            result.extend(b)
        return result



    @staticmethod
    def traverse_inorder(root: TreeNode) -> List[int]:
        if not root:
            return []
        result: List[int] = []
        visited: List[TreeNode] = []
        stack: List[TreeNode] = [root]
        while stack:
            current = stack[-1]
            if current.left and current.left not in visited:
                stack.append(current.left)
                continue
            result.append(current.val)
            visited.append(stack.pop())
            if current.right and current.right not in visited:
                stack.append(current.right)
        return result



class Solution2:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, output = [], [], []

        while root1 or root2 or stack1 or stack2:
            # update both stacks
            # by going left till possible
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            # Add the smallest value into output,
            # pop it from the stack,
            # and then do one step right
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                output.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                output.append(root2.val)
                root2 = root2.right

        return output
