#!/usr/bin/env python3

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3

- Runs in O(n) time - every node is visited exactly once.
- Uses O(1) space - we don't grow any data structures.

- This is a good follow-up to the original 'remove duplicates from sorted list' problem.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28335/My-accepted-Java-code
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        fakeHead = ListNode(0)
        fakeHead.next = head

        pre = fakeHead
        curr = head

        while curr is not None:
            # Move curr ahead if its next value is a duplicate.
            while curr.next is not None and curr.val == curr.next.val:
                curr = curr.next

            # If pre is right behind curr, move pre ahead.
            if pre.next == curr:
                pre = pre.next
            # Otherwise, pre and curr are separated by duplicates. So,
            # skip those duplicates.
            else:
                pre.next = curr.next

            # When this loop completes, all nodes before curr
            # are non-duplicates in the original list.
            curr = curr.next

        return fakeHead.next

    def test(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(2)
        l1.next.next.next = ListNode(3)
        l1.next.next.next.next = ListNode(3)
        l1.next.next.next.next.next = ListNode(4)

        deduped1 = self.deleteDuplicates(l1)
        self._printLinkedList(deduped1)

        l2 = ListNode(1)
        l2.next = ListNode(1)
        l2.next.next = ListNode(2)
        l2.next.next.next = ListNode(3)

        deduped2 = self.deleteDuplicates(l2)
        self._printLinkedList(deduped2)

    def _printLinkedList(self, head):
        curr = head
        while curr is not None:
            print(curr.val)
            curr = curr.next


sol = Solution()
sol.test()
