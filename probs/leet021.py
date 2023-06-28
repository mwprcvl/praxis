#!/usr/bin/env/python3

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class ListNode:
    """ """

    def __init__(self, val=0, next=None):
        """ """
        self.val = val
        self.next = next


class Solution:
    """ """

    def solve(self, list1: ListNode, list2: ListNode) -> ListNode:
        """ """
        if not list1 and not list2:
            return []
        merged = ListNode()
        head = merged
        while list1 and list2:
            if list1.val < list2.val:
                head.next = ListNode(list1.val)
                list1 = list1.next
            else:
                head.next = ListNode(list2.val)
                list2 = list2.next
            head = head.next
        head.next = list1 if list1 else list2
        return merged.next


def nodevals_to_list(res):
    """ helper function for test cases """
    result = []
    head = res
    while head:
        result.append(head.val)
        head = head.next
    return result


sol = Solution()

l_1 = ListNode(1, ListNode(2, ListNode(4)))
l_2 = ListNode(1, ListNode(3, ListNode(4)))
expect = [1, 1, 2, 3, 4, 4]
assert nodevals_to_list(sol.solve(l_1, l_2)) == expect

expect = []
assert nodevals_to_list(sol.solve(None, None)) == expect

expect = [0]
assert nodevals_to_list(sol.solve(ListNode(0), None)) == expect
