#!/usr/bin/env python3

"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?


- Runs in O(n) time.
- Uses O(n) space.

- There's an alternative solution that modifies the BST node to track the rank of each node. The initial traversal that sets all the ranks will take O(n), but subsequent lookups will take O(log n).
    - The follow up diminishes the time savings of this alternative, since the BST nodes will need to be re-ranked before finding the kth smallest on a modified tree. However, its running time is pretty close to O(n) and it uses O(1) space, so it's still a more optimal solution. I'll implement that when I review this problem next time.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        numbers = []
        self.collectNumbers(root, numbers)
        return numbers[k - 1]

    def collectNumbers(self, root, numbers):
        if root is None:
            return

        self.collectNumbers(root.left, numbers)
        numbers.append(root.val)
        self.collectNumbers(root.right, numbers)

    def test(self):
        t1 = TreeNode(3)
        t1.left = TreeNode(1)
        t1.right = TreeNode(4)
        t1.left.right = TreeNode(2)

        assert self.kthSmallest(t1, 1) == 1

        t2 = TreeNode(5)
        t2.left = TreeNode(3)
        t2.right = TreeNode(6)
        t2.left.left = TreeNode(2)
        t2.left.right = TreeNode(4)
        t2.left.left.left = TreeNode(1)

        assert self.kthSmallest(t2, 3) == 3

        print('All tests passed!')


sol = Solution()
sol.test()
