#!/usr/bin/env python3

"""
https://leetcode.com/problems/partition-list

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5


- Runs in O(n) time.
- Uses O(1) space.
- Good pattern to know to extract sublists.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Edge case.
        if head is None or head.next is None:
            return None

        # Pointers that help build the 2 halves.
        h1 = t1 = None
        h2 = t2 = None

        curr = head
        while curr is not None:
            if curr.val < x:
                if h1 is None:
                    h1 = t1 = curr
                else:
                    t1.next = curr
                    t1 = curr
            else:
                if h2 is None:
                    h2 = t2 = curr
                else:
                    t2.next = curr
                    t2 = curr

            curr = curr.next

        # If all values are >= x.
        if h1 is None:
            return h2
        # If all values are < x.
        elif h2 is None:
            return h1

        # Concatenate the 2 halves.
        t2.next = None
        t1.next = h2

        return h1

    def test(self):
        head = self._buildList([1, 4, 3, 2, 5, 2])
        self._printLinkedList(self.partition(head, 3))

    def _buildList(self, l):
        head = ListNode(l[0])

        if len(l) == 1:
            return head

        curr = head
        for i in range(1, len(l)):
            curr.next = ListNode(l[i])
            curr = curr.next

        return head

    def _printLinkedList(self, head):
        curr = head
        while curr is not None:
            print(curr.val)
            curr = curr.next

sol = Solution()
sol.test()
