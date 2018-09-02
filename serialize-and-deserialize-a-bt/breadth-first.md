# Serialize and Deserialize a BT - Breadth-First

* [Serialize and Deserialize Binary Tree - LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/)

## Algorithm

* Say we serialize it as a string

```py
class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
```

### Serialize

* Traverse the BT in a breadth-first manner using a queue
* For each node
	* If the node’s value is null, append a ‘?’ and a comma to the string
	* Else, append the node’s value and a comma to a string
* Starting from the back of the string, remove all ‘?’ and ‘,’
* Return the string

```py
def serialize(root):
	# Base case.
	if root is None: return ''

	q = Queue()
	s = ''
	q.put(root)

	while not q.empty():
		curr = q.get()
		if curr is None:
			s += '?,'
		else:
			s += str(curr.val) + ','
			q.put(curr.left if curr.left else None)
			q.put(curr.right if curr.right else None)

	# Remove multiple trailing '?' and ','.
	j = 0
	for i in range(len(s) - 1, -1, -1):
		if s[i] is ',' or s[i] is '?':
			j += 1
		else:
			break

	# Hacking of indices to slice the string properly.
	return s[0:-1-j+1]
```

### Deserialize

* Split the string into an array
* Pop the first element off the array and make it the root node
* Initialize `visited_left` and `visited_right` as `False` - these are flags to mark that left and right children respectively have been visited
* Make `curr` a reference to the root node
* For each remaining element in the array
	* If not `visited_left`
		* If elem is not ‘?’, assign it to `curr.left`
		* Mark `visited_left` as `True`
	* Else if not `visted_right`
		* If elem is not ‘?’, assign it to `curr.left`
		* Mark `visited_right` as `True`
	* Else
		* Put `curr.left` and `curr.right` into the queue, if they’re not null
		* Get the next queued elem and assign it to `curr`
		* If elem is not ‘?’, assign it to `curr.left`
		* Mark `visited_right` as `False`
* Return root

```py
def deserialize(s):
	# Base case.
	if len(data) == 0: return None

	q = Queue()
	lst = s.split(',')
	root = TreeNode(lst[0])
	curr = root
	visited_left = visited_right = False

	for i in range(1, len(lst)):
		if not visited_left:
			if lst[i] is not '?':
				curr.left = TreeNode(lst[i])
			visited_left = True
		elif not visited_right:
			if lst[i] is not '?':
				curr.right = TreeNode(lst[i])
			visited_right = True
		else:
			if curr.left is not None: q.put(curr.left)
			if curr.right is not None: q.put(curr.right)
			curr = q.get()
			if lst[i] is not '?':
				curr.left = TreeNode(lst[i])
			# Because we've just visited left.
			visited_right = False

	return root
```

## Complexity

### Serialize

* Time: `O(n)` - visit every node once
* Space: `O(log_2 n + k - 1)` -> `O(log_2 n)`
	* `log_2 n` is the height of a full BT, where `k` is the number of commas used

### Deserialize

* Time: `O(n)` - where `n` is the number of elements delimited by ‘,’
* Space: `O(n)` - number of nodes in returned BT

## Comments

* I chose to traverse the BT bread-first because it yields a more intuitive string representation - however, I found it harder to implement breadth-first traversal than depth-first traversal
* Easy to infer that the element at index `k` is the parent of elements at index `2k + 1` and `2k + 2`
