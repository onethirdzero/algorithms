# Counting Unival Subtrees - O(n)

* [Counting Unival Subtrees · Daily Coding Problem](https://www.dailycodingproblem.com/blog/unival-trees/)

## Algorithm

* If current node is None, return (False, 0)
* If current node is leaf, return (True, 1)
* Else
	* If left and right subtrees are unival and current node’s value matches the children’s value
		* Return (True, left + right + 1)
	* Else, return (False, left + right)

## Complexity

* Time: `O(n)` - we visit every node only once
* Space: `O(1)`

## Comments

* I was surprised that I arrived at an optimal solution first, albeit with some redundant code
* After looking at the naive solution, I thought the optimal was more intuitive to figure out on the first try - but probably only because I've looked at a tree problem that had a similar structure before
* I later realized that both solutions have the same traversal strategy, and differ only in how they verify unival subtrees

* The key is to recognize what conditions need to be true for a subtree to be unival - going through examples was helpful for this
* Knowing what extra info to be passed back up the recursion was helpful too - similar to ‘Deepest node in a BT’ problem
