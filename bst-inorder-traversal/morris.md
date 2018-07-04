# BST Inorder Traversal - Morris Traversal

* * [Validate Binary Search Tree - LeetCode](https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution))

## Algorithm

* while `curr` is not `None`:
	* if left child does not exist:
		* visit `curr`
		* move `curr` to its right child
	* else:
		* go to rightmost node of `curr`’s left subtree (predecessor aka `pred` of `curr`, making sure we don’t reach `curr`)
		* if `pred`’s right child does not exist:
			* link `pred` to `curr` by making `curr` `pred`’s right child
			* move `curr` to its left child
		* else:
			* remove the link  between `pred`’s right child and `curr`
			* visit `curr`
			* move `curr` to its right child

## Complexity

* `O(1)` space
* `O(n)` time

## Comments

* We’re slightly modifying the tree, but we fix it on the way back
	* Uses a concept called threaded binary tree
	* The links are established so that we have a way to backtrack
* This was super helpful for developing the intuition: [Morris Inorder Tree Traversal - YouTube](https://www.youtube.com/watch?v=wGXB9OWhPTg)
* Discovered this while trying to understand the Morris solution for BST validation
	* To develop that solution, replace the ‘visit’ part with a check on the `previous` node and a comparison of `curr`’s and `previous`’s values, then make sure to make `curr` the new `previous`
* Does not work if the tree has duplicate values?
