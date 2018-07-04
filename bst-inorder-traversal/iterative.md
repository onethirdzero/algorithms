# BST Inorder Traversal - Iterative

* [Validate Binary Search Tree - LeetCode](https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution))

## Algorithm

* while `curr` is not `None` and `stack` is not empty:
	* while `curr` is not `None`:
		* add `curr` to stack
		* move `curr` to left child
	* pop from stack into `curr` (we’re in at `None`)
	* visit `curr`
	* move `curr` to right child

## Complexity

* `O(n)` time
* `O(n)` space
	* If it’s all left children or all right children, then the stack would contain the full tree

## Comments

* Helpful as a foundation for BST questions that require traversing the tree
* The recursive version is trivial, but modifying it could be tricky
* Discovered this when I was trying to solve a BST validation problem
	* To develop that solution, replace the ‘visit’ step with a check of whether `previous` (global value) is `None` and a comparison of `previous` and `curr`’s values
