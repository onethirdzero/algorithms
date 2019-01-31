#!/usr/bin/env python3
"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node

Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:
- You may only use constant extra space.
- Recursive approach is fine, implicit stack space does not count as extra space for this problem.
- You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

Example:
Given the following perfect binary tree,
     1
   /  \
  2    3
 / \  / \
4  5  6  7

After calling your function, the tree should look like:
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class IterativeSolution:
    """
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37461/Java-solution-with-O(1)-memory+-O(n)-time/163738

    - Runs in O(n) time.
    - Uses O(1) space.

    - An important pattern to learn here is looking ahead further than a single 'hop' - eg. curr.right.next
    - The magic step: the rightmost node, B, in the left half of level k is able to reach the leftmost node in the right half of level k because B's parent (in level k - 1) already has its .next pointer pointed correctly.

        k - 1       X ----> Y
                   / \     / \
        k         A   B   C   D

    - Not sure how to test this programmatically. I'll come back to this next time.
    """

    def connect(self, root):
        level_start = root

        while level_start is not None:
            curr = level_start

            while curr is not None:
                if curr.left is not None:
                    curr.left.next = curr.right
                if curr.right is not None and curr.next is not None:
                    # Magic step here.
                    # curr.next points to some left subtree adjacent to it,
                    # on its right.
                    curr.right.next = curr.next.left

                curr = curr.next

            level_start = level_start.left


class RecursiveSolution:
    """
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37461/Java-solution-with-O(1)-memory+-O(n)-time/163738

    - Runs in O(n) time.
    - Uses O(1) space.

    - Magic step is identical to the iterative solution.
    """

    def connect(self, root):
        if root is None:
            return

        if root.left is not None:
            root.left.next = root.right
        if root.right is not None and root.next is not None:
            # Magic step.
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)
