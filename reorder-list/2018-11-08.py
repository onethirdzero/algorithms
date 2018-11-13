#!/usr/bin/env python3

"""
https://leetcode.com/problems/reorder-list/description/

Given a singly linked list L: L0->L1->...->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...

You may not modify the values in the list's nodes, only nodes itself may be changed.

eg. Given 1->2->3->4, reorder it to 1->4->2->3.
eg. Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

- Runs in O(2n) -> O(n) time.
- Uses O(1) space - only pointer manipulation.
- The fast and slow pointer is a useful trick for finding the middle of a linked list.
- The interleave step is just a more straightforward merge of two linked lists.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # https://www.programcreek.com/2013/12/in-place-reorder-a-singly-linked-list-in-java/
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        # Find the middle of the list.
        middle = self._findMiddle(head)

        # Split the original list in half.
        second = middle.next
        middle.next = None

        # Reverse the second half.
        second = self._reverse(second)

        # Interleave the two halves into a merged list.
        head = self._interleave(head, second)

    def _findMiddle(self, head):
        # Returns the middle node of the given list such that
        # length of first half >= length of second half.
        p1 = head  # Slow pointer.
        p2 = head  # Fast pointer.

        # Step only if the fast pointer can step forward.
        while p2.next is not None and p2.next.next is not None:
            p1 = p1.next
            p2 = p2.next.next

        return p1

    def _reverse(self, head):
        # Reverses the given list in-place and
        # returns the head of the reversed list.
        pre = head
        curr = head.next

        while curr is not None:
            # Reverse the pointers.
            temp = curr.next
            curr.next = pre
            # Step the pointers forward.
            pre = curr
            curr = temp

        # Get rid of the cycle near the head of the original list.
        head.next = None

        return pre

    def _interleave(self, a, b):
        # Returns an interleaved list, which is
        # the result of interleaving the two given lists in-place.
        p1 = a
        p2 = b

        while p2 is not None:
            t1 = p1.next
            t2 = p2.next

            p1.next = p2
            p2.next = t1

            p1 = t1
            p2 = t2

        return a

    def test(self):
        # 1->2->3->4->5
        h = ListNode(1)
        h.next = ListNode(2)
        h.next.next = ListNode(3)
        h.next.next.next = ListNode(4)
        h.next.next.next.next = ListNode(5)

        self.reorderList(h)

        curr = h
        while curr is not None:
            print(curr.val)
            curr = curr.next


sol = Solution()
sol.test()
