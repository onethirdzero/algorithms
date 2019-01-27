#!/usr/bin/env python3
"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given:

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class RecursiveSolution:
    """
    https://leetcode.com/articles/construct-binary-tree-from-preorder-and-inorder-tr/

    - O(n^2) time
        - O(n) search for root index, O(n - 1) construction of inorder list for left and right recursion - repeated O(n) times.
    - O(n) space?
        - Space taken up on the recursion stack?

    - The key is to know that the first element of the preorder list is the root, and that the root's index partitions the inorder list into left and right subtree elements - having that is enough for recursion to do the rest magically.

    - Running time can apparently be improved: leetcode.com/articles/construct-binary-tree-from-preorder-and-inorder-tr/188853/Construct-binary-tree-from-preorder-and-inorder-traversal/201314
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def helper(preorder, inorder):
            if not inorder:
                return None

            # The first element of preorder is always a root.
            root_val = preorder.popleft()
            root = TreeNode(root_val)

            # The root's index splits inorder into left and right subtree elements.
            index = inorder.index(root.val)

            root.left = helper(preorder, inorder[:index])
            root.right = helper(preorder, inorder[index + 1:])

            return root

        return helper(deque(preorder), inorder)


class IterativeSolution:
    """
    https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34555/The-iterative-solution-is-easier-than-you-think!/221653

    - Runs in O(n) time - every element in the preorder list is visited once.
    - Uses O(k) space.
        - The stack contains at most 2 elements (from the top): left subtree node, left subtree parent.

    - The pattern is similar to the recursive approach.
    - Probably only works on a BT - it would need more prev variables otherwise.
    - An important point is to append TreeNodes to the stack, so that the half-built subtrees can be retained.
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return None

        # Track the root so it can be returned.
        root = TreeNode(preorder[0])
        stack = []
        stack.append(root)

        pre_index = 1
        ino_index = 0
        while (pre_index < len(preorder)):
            curr = TreeNode(preorder[pre_index])
            pre_index += 1
            prev = None

            # While stack is not empty and the top of the stack
            # is not equal to ino.
            while stack and stack[-1].val == inorder[ino_index]:
                prev = stack.pop()
                ino_index += 1

            if prev:
                # Add right subtree.
                prev.right = curr
            else:
                # Add left subtree.
                stack[-1].left = curr

            stack.append(curr)
        return root


def test():
    def preorderTraverse(root, result):
        """Record the preorder traversal of root to result"""

        if root is None:
            return

        result.append(root.val)
        preorderTraverse(root.left, result)
        preorderTraverse(root.right, result)

        return

    def inorderTraverse(root, result):
        """Record the inorder traversal of root to result"""
        if root is None:
            return

        inorderTraverse(root.left, result)
        result.append(root.val)
        inorderTraverse(root.right, result)

        return

    def actualTest(builtRoot):
        test_pre = []
        test_ino = []

        preorderTraverse(builtRoot, test_pre)
        inorderTraverse(builtRoot, test_ino)

        assert pre == test_pre
        assert ino == test_ino

    # Actual test data.
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]

    root_recursive = RecursiveSolution().buildTree(pre, ino)
    root_iterative = IterativeSolution().buildTree(pre, ino)

    actualTest(root_recursive)
    actualTest(root_iterative)

    print('All tests passed!')

test()
