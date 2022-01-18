# Definition for singly-linked list.
# import wsgiref.validate
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        cur = head = ListNode()
        while l1 and l2:
            # print(l1.val, l2.val, cur.val)
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return head.next


class Solution1:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result: ListNode = None
        end_result: ListNode = None

        def add_node(node: ListNode):
            nonlocal result, end_result
            if result is None:
                result = node
                end_result = result
            elif node is None:
                print("Attempt to add None instead ListNode.")
                return
            else:
                end_result.next = node
                end_result = node

        def queue(start: ListNode) -> ListNode:
            if start is None:
                yield None
            end = start
            while end is not None:
                yield end
                end = end.next
            else:
                yield None

        q1 = queue(l1)
        q2 = queue(l2)
        c1 = next(q1)
        c2 = next(q2)
        while c1 is not None or c2 is not None:
            # print('c1 ->', c1.val if c1 is not None else None, ' : c2 ->', c2.val if c2 is not None else None)
            # sleep(0.5)
            if c1 is not None and c2 is not None:
                if c1.val <= c2.val:
                    add_node(c1)
                    c1 = next(q1)
                    continue
                else:
                    add_node(c2)
                    c2 = next(q2)
                    continue
            if c1 is not None and c2 is None:
                add_node(c1)
                c1 = next(q1)
                continue
            if c1 is None and c2 is not None:
                add_node(c2)
                c2 = next(q2)
                continue
        return result


def nodeVal_to_list(node: ListNode) -> List[ListNode]:
    lst = []
    while node is not None:
        lst.append(node)
        node = node.next
    return [x.val for x in lst]


l8 = ListNode(83, None)
l7 = ListNode(67, l8)
l6 = ListNode(62, l7)
l5 = ListNode(53, l6)
l4 = ListNode(4, l5)
l3 = ListNode(3, l4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)

r8 = ListNode(80, None)
r7 = ListNode(70, r8)
r6 = ListNode(60, r7)
r5 = ListNode(50, r6)
r4 = ListNode(40, r5)
r3 = ListNode(30, r4)
r2 = ListNode(5, r3)
r1 = ListNode(3, r2)


def side_by_side(a: ListNode, b: ListNode) -> ListNode:
    res = a
    end_res = res
    cur_a = a.next  # current start 1st queue
    a_fur = cur_a.next  # next in 1st queue
    cur_b = b  # current start 2nd queue
    b_fur = cur_b.next  # next in 2nd queue

    while cur_a is not None or cur_b is not None:
        # print(cur_b.val, cur_a.val)
        if cur_b is not None:
            end_res.next = cur_b
            end_res = end_res.next
            cur_b = b_fur
            b_fur = cur_b.next if cur_b is not None else None
        if cur_a is not None:
            end_res.next = cur_a
            end_res = end_res.next
            cur_a = a_fur
            a_fur = cur_a.next if cur_a is not None else None

# print(nodeVal_to_list(Solution.mergeTwoLists(None, l1, r2)))

# result = side_by_side(l1, r1)
# print(nodeVal_to_list(result))

# q = queue(l1)
# x = next(q)
# print('Elem: ->', x.val if x is not None else 'None')
# while x is not None:
#     x = next(q)
#     print('Elem: ->', x.val if x is not None else 'None')
