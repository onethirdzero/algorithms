#!/usr/bin/env python3

"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

 - Runs in O(n log n) time
    - Finding the midpoint takes O(n/2) => O(n) time.
    - We do this on smaller and smaller n each time. More specifically, n shrinks by half on each recursive call.
    - We make log n recursive calls, because we can only split the inputs log n times.
    - So, an O(n) operation repeated log n times gets us O(n log n) total run time.
- Uses O(log n) space?
    - Because we're constructing the tree in a balanced way, we don't ever build a skewed tree.
    - This bounds the height of the tree to O(log n).
    - But aren't we creating n nodes to store all elements?

- There are 2 other approaches that improve run time and storage. I'll get to those next time. Incomplete.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # https://leetcode.com/articles/convert-sorted-list-to-binary-search-tree/
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None

        # Find midpoint.
        mid = self._splitAtMid(head)

        # Make that a root node.
        root = TreeNode(mid.val)

        # If list is only length-1.
        if head == mid:
            return root

        # Recurse on left and right halves and attach them as children to root.
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root

    def _splitAtMid(self, head):
        """
        Splits the given linked list into two halves and returns the
        head of the second half.
        """
        # Prev will point to the tail of the first half.
        # It moves at the same pace as slow.
        prev = None

        # Find the midpoint using slow and fast pointers.
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # If slow stayed at head, prev wouldn't have moved either.
        if prev is not None:
            # Split the lists.
            prev.next = None

        return slow

    def test(self):
        x = ListNode(-10)
        x.next = ListNode(-3)
        x.next.next = ListNode(0)
        x.next.next.next = ListNode(5)
        x.next.next.next.next = ListNode(9)

        root = self.sortedListToBST(x)
        print('Inorder traversal of BST:')
        self._printTree(root)

    def _printTree(self, root):
        if root is None:
            return

        self._printTree(root.left)
        print(root.val)
        self._printTree(root.right)

sol = Solution()
sol.test()
