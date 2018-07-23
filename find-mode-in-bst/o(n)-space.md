# Find Mode in BST - O(n) Space

* https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
* Mode is the most commonly occurring value

## Algorithm

* Traverse BST
	* At each node, add keys to a hash table
* `mode_count` = max value in the hash table
* If a value in the hash table matches `mode_count`, append it to `modes`
* Return `modes`

## Complexity

* Time: `O(n)`
* Space: `O(n)`
	* In the worst case, we have all unique values

## Comments

* This should have been trivial, but I struggled with dealing with multiple modes
* But this is a useful pattern to know if you need multiple occurrences of a particular value: run through the inputs and pick out keys whose value matches the desired
