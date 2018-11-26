#!/usr/bin/env python3

"""
https://leetcode.com/problems/subtree-of-another-tree/

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2

Given tree t:
   4
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:
   4
  / \
 1   2

Return false.

- Runs in O(n) time.
- Uses O(1) space.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            return False

        if s.val == t.val:
            # Start traversing both trees.
            if self._match(s, t):
                return True

        # Keep looking for a starting point.
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def _match(self, s, t):
        # If both are leaves.
        if s is None and t is None:
            return True

        # If only one is a leaf.
        if s is None or t is None:
            return False

        if s.val != t.val:
            return False

        # Keep moving ahead in tandem.
        return self._match(s.left, t.left) and self._match(s.right, t.right)

    def test(self):
        t1 = TreeNode(1)
        t1.next = TreeNode(1)
        t2 = TreeNode(1)

        print(self.isSubtree(t1, t2))

sol = Solution()
sol.test()
