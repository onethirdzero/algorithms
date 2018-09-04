# Counting Unival Subtrees - O(n^2)

* [Counting Unival Subtrees · Daily Coding Problem](https://www.dailycodingproblem.com/blog/unival-trees/)

## Algorithm

* To check if a subtree is unival, visit each node and check if the subtree rooted at that node is unival

* Traverse the tree
* At each node
    * If node is null, return 0
    * Count the unival subtrees in the right subtree
    * Count the unival subtrees in the right subtree
    * If the current node's subtree is unival, return left count + right count + 1
    * Else, return left + right

## Complexity

* Time: O(n^2)
    * On the way back up the recursion, we check if the current subtree is unival by visiting each of its nodes
* Space: O(1)

## Comments

* The redundancy comes from visiting each node of a subtree rooted at the current node when we've already verified that its left and right subtrees are unival
* We can encode whether or not the left and right subtrees are unival by having them return a flag along with their count of unival subtrees
