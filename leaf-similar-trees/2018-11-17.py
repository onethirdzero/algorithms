#!/usr/bin/env python3

"""
https://leetcode.com/problems/leaf-similar-trees/

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
Both of the given trees will have between 1 and 100 nodes.


- Runs in O(n) time, since we visit every node.
- Uses O(k) space, where k is the maximum number of leaves between the given trees.
- We assume that the trees aren't guaranteed to have the same structure or depth.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves_1 = []
        leaves_2 = []

        # Traverse both trees, collecting their leaf value sequences.
        self._traverse(root1, leaves_1)
        self._traverse(root2, leaves_2)

        # Compare leaf sequences.
        if len(leaves_1) != len(leaves_2):
            return False

        for i in range(len(leaves_1)):
            if leaves_1[i] != leaves_2[i]:
                return False

        return True

    def _traverse(self, root, leaves):
        """Traverses a tree in a depth-first manner, writing all the leaf values to the given list.
        :type roo1: TreeNode
        :type leaves: list
        :rtype: None
        """
        if root is None:
            return
        if root.left is None and root.right is None:
            # We're at a leaf.
            leaves.append(root.val)

        # Move on to children.
        self._traverse(root.left, leaves)
        self._traverse(root.right, leaves)

    def test(self):
        t1 = TreeNode(3)
        # Left subtree.
        t1.left = TreeNode(5)
        t1.left.left = TreeNode(6)  # Leaf.
        t1.left.right = TreeNode(2)
        t1.left.right.left = TreeNode(7) # Leaf.
        t1.left.right.right = TreeNode(4)  # Leaf.

        # Right subtree.
        t1.right = TreeNode(1)
        t1.right.left = TreeNode(9)  # Leaf.
        t1.right.right = TreeNode(8)  # Leaf.

        t2 = TreeNode(3)
        # Left subtree.
        t2.left = TreeNode(5)
        t2.left.left = TreeNode(6)  # Leaf.
        t2.left.right = TreeNode(7)  # Leaf.

        # Right subtree.
        t2.right = TreeNode(1)
        t2.right.left = TreeNode(4) # Leaf.
        t2.right.right = TreeNode(2)
        t2.right.right.left = TreeNode(9)  # Leaf.
        t2.right.right.right = TreeNode(8)  # Leaf.

        print(self.leafSimilar(t1, t2))

sol = Solution()
sol.test()
