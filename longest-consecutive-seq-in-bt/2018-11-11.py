"""
https://www.geeksforgeeks.org/longest-consecutive-sequence-binary-tree/

Given a binary tree, find the length of the longest path which comprises of nodes with consecutive values in increasing order. Every node is considered as a path of length 1.

- Runs in O(n) time.
- Uses O(1) space.
- I found this on Program Creek first (https://www.programcreek.com/2014/04/leetcode-binary-tree-longest-consecutive-sequence-java/), and was confused by the wording of the question - I thought I just had to find the length of the longest root-to-leaf path.
- I'm not too happy with modifying some global variable (longest), but trying to change that seems to quickly make the code less readable.
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    longest = 0

    def longestConsecutiveSeq(self, root):
        if root is None:
            return 0

        self.helper(root, root.val, 1)
        return self.longest

    def helper(self, root, expected, currLength):
        if root is None:
            return

        # Check if current node's value is consecutive.
        if root.val is expected:
            currLength += 1
        else:
            currLength = 1

        # Update longest so far.
        self.longest = max(self.longest, currLength)

        # Check left and right children.
        self.helper(root.left, root.val + 1, currLength)
        self.helper(root.right, root.val + 1, currLength)

    def test(self):
        r = Node(6)
        r.right = Node(9)
        r.right.left = Node(7)
        r.right.right = Node(10)
        r.right.right.right = Node(11)

        seq = self.longestConsecutiveSeq(r)
        print(seq)

sol = Solution()
sol.test()
