#!/usr/bin/env python3

"""
https://leetcode.com/problems/binary-tree-level-order-traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


- Runs in O(n) time.
- Uses O(n) space.
    - A full BT of n nodes has exactly (n+1)/2 leaves, which is the maximum number of nodes ever in the queue.

- The important bit here is to use the size of the queue to partition nodes in the queue - this lets us only look at nodes belonging to the current level at each iteration, while simultaneously collecting children for the next level.
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = deque()
        result = []

        if root is None:
            return result

        q.append(root)
        while len(q) != 0:
            # This partitions the nodes in the queue so that we only look at
            # nodes belonging to the current level.
            curr_level_node_count = len(q)
            curr_level_nodes = []

            # Collect children of nodes in the current level, which
            # will go into the next level.
            for _ in range(curr_level_node_count):
                current = q[0]

                if current.left is not None:
                    q.append(current.left)
                if current.right is not None:
                    q.append(current.right)

                curr_level_nodes.append(q.popleft().val)

            # Add all nodes in the current level to result.
            result.append(curr_level_nodes)

        return result

    def test(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        print(self.levelOrder(root))


sol = Solution()
sol.test()
