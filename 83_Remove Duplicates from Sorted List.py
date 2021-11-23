# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def generate_sequence(seq: List[int]) -> Optional[ListNode]:
    head = cur = None
    for x in seq:
        if cur is None:
            head = cur = ListNode(x)
            continue
        cur.next = ListNode(x)
        cur = cur.next
    return head



class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node: ListNode = head
        while cur_node is not None and cur_node.next is not None:
            if cur_node.val == cur_node.next.val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return head
