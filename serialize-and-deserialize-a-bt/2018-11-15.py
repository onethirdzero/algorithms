#!/usr/bin/env python3

"""
https://leetcode.com/problems/serialize-and-deserialize-bst/description/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

- If we do a preorder traversal to serialize the tree, we get a string that looks like:
    rootValue | (<rootValue) (<rootValue) (<rootValue) | (>rootValue) (>rootValue)
- We can take advantage of this structure when deserializing.

- On each recursive call of _getNode(), we create a root node, then values for
the left and right subtrees. Q will contain values for the left subtree and smallerQ
will contain values for the right subtree.
- The recursion then builds the left subtree first, then the right subtree,
before joining both to the root.

- Runs in O(n^2) time?
    - On each call to _getNode(), we add n - 1 values to smallerQ.
    - n + (n - 1) + ... + 1 = n * (n - 1) / 2 => O(n^2) is my best guess.
    - But aren't we operating on 1 input on each recursive call? Doesn't
    this reduce the input linearly?
- Uses O(n) space.
    - An unbalanced tree will fill up the queue with only values smaller than
    root or only values larger than root.

- Still doesn't work for some test cases on LeetCode. Incomplete.
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/93175/Java-PreOrder-+-Queue-solution

    # Constants.
    DELIMITER = ';'
    NULL = "null"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return self.NULL

        serialized = ''
        stack = []
        stack.append(root)

        while len(stack) != 0:
            # Serialize root.
            root = stack.pop()
            serialized += str(root.val) + self.DELIMITER

            # Serialize left and right children if they exist.
            # We serialize the right subtree first.
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

        # Remove the trailing delimiter before returning.
        return serialized[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == self.NULL:
            return None

        node_data = data.split(self.DELIMITER)
        Q = deque()
        for item in node_data:
            Q.append(item)
        return self._getNode(Q)

    def _getNode(self, Q):
        """Helper function that returns a deserialized tree
        from a queue of tree node data.

        :type Q: queue.Queue
        :rtype: TreeNode
        """
        # This helps us avoid adding nodes beyond a leaf.
        if len(Q) == 0:
            return None

        root = TreeNode(Q.popleft())
        smallerQ = deque()

        # Take values smaller than root.val.
        while len(Q) != 0 and Q[0] < root.val:
            smallerQ.append(Q.popleft())

        # Build left subtree.
        root.left = self._getNode(smallerQ)
        # Build right subtree.
        root.right = self._getNode(Q)

        return root

    def test(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.right = TreeNode(6)
        root.right.right = TreeNode(7)

        serialized = self.serialize(root)
        print(serialized)

        deserialized = self.deserialize(serialized)
        print('Preorder traversal: ')
        self._printPreorderTree(deserialized)

    def _printPreorderTree(self, root):
        """Does a preorder traversal of the tree and prints each node
        along the way.
        """
        print(root.val + ' ')
        if root.left is not None:
            self._printPreorderTree(root.left)
        if root.right is not None:
            self._printPreorderTree(root.right)


sol = Codec()
sol.test()
