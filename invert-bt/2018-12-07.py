#!/usr/bin/env python3

"""
Invert a binary tree.

Example:
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.


- Runs in O(n) time.
- Uses O(1) space.

- Just thought it might be fun to see if I'm even remotely Google-material.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        # Swap children.
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)

        return root

    def test(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        self._printTree(self.invertTree(root))

    def _printTree(self, root):
        """
        Does a preorder traversal and prints nodes in a given tree.
        """
        if root is None:
            return

        print(root.val)
        self._printTree(root.left)
        self._printTree(root.right)

sol = Solution()
sol.test()
