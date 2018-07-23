# Find Mode in BST - O(1) Space

* [Find Mode in Binary Search Tree - LeetCode](https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/98101/Proper-O(1)-space)

## Algorithm

* Traverse the BST, finding the highest number of occurrences of any value
* Traverse the BST again to collect all values occurring that often

```py
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	curr_val = 0
	curr_count = 0
	max_count = 0
	mode_count = 0
	modes = None

	def findMode(self, root):
		inorder(root)
		self.modes = []
		self.mode_count = 0
		self.curr_count = 0
		inorder(root)
		return modes

	def handleValue(self, val):
		if val != self.curr_val:
			# New value.
			self.curr_val = val
			self.curr_count = 0
		# Count every node.
		self.curr_count += 1

		# New mode!
		if self.curr_count > self.max_count:
			self.max_count = self.curr_count
			self.mode_count = 1 # Because we have a new high.
		elif self.curr_count == self.max_count:
			if self.modes is not None:
				# This only runs on the 2nd pass.
				# The first time this runs, mode_count is 0, so no worries about an out of bounds index.
				self.modes[mode_count] = self.curr_val
			self.mode_count += 1

	def inorder(self, root):
		if root is None: return
		inorder(root.left)
		handleValue(root.val)
		inorder(root.right)
```

## Complexity

* Time: `O(n)`
* Space: `O(1)`

## Comments

* A useful pattern here is to realize that multiple passes of a BST won’t change the `O(n)` time complexity
* Here, we disregard the space cost of the return space as well as the recursion stack space (if recursion is used)

* Duplicates will be located near each other thanks to the BST property - so we don’t have to worry about tracking more than 1 key at a time
* Once `curr_val` changes, we won’t see it again elsewhere in the BST

* `inorder()`’s implementation can be substituted for a Morris traversal implementation - for proper `O(1)` space complexity
