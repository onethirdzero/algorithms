# Deepest Node in a BT - Recursive

* [How to Formulaically Solve Tree Interview Questions · Daily Coding Problem](https://www.dailycodingproblem.com/blog/how-to-formulaically-solve-tree-interview-questions/)

## Algorithm

* If node is not null and left child is empty and right child is empty
	* Return current node and depth of 1
* If left child is empty
	* Find the deepest node in the right subtree and increment its depth by 1, then return the result
* If right child is empty
	* Find the deepest node in the left subtree and increment its depth by 1, then return the result
* Take the max of the deepest nodes in left and right subtrees and increment its depth by 1, then return the result

```py
def deepest(node):
	if node and not node.left and not node.right:
		# Base case.
		return (node, 1)

	if not node.left:
		# The deepest node is in the right subtree.
		n, d = deepest(node.right)
		return (n, d + 1)
	elif not node.right:
		# The deepest node is in the left subtree.
		n, d = deepest(node.left)
		return (n, d + 1)

	# Choose the deepest node among the subtrees.
	n, d = max(
		deepest(node.left),
		deepest(node.right),
		key=lambda x: x[1]
	)
	return (n, d + 1)
```

## Complexity

* Time: `O(n)`?
	* I think we only visit each node once
* Space: `O(1)`

## Comments

* Try not to get too caught up in implementing the recursion - just trust that it will return the correct answer and act on it
* Focus on figuring out what information we need to solve the problem - this will lead you to crafting the base case’s structure

* The base case’s return value shows what we will manipulate in the recursive step
	* Here we chose to include the depth and the leaf node in the return value - those will be the only data we have access to
