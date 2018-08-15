# Path Sum III - O(n) Prefix Sum Method

* https://leetcode.com/problems/path-sum-iii/description/

## Algorithm

* https://leetcode.com/problems/path-sum-iii/discuss/91878/17-ms-O(n)-java-Prefix-sum-method

```py
count = 0

def pathSum(root, sum):
	pre_sum = {}
	pre_sum[0] = 1 # Base case where curr_sum == target.
	helper(root, 0, sum, pre_sum)
	return count

def helper(root, curr_sum, target, pre_sum):
	if root is None: return

	curr_sum += root.val

	# If the remainder of curr_sum - target is a valid path,
	# that means curr_sum contains nodes that will sum up
	# to target.
	if (curr_sum - target) in pre_sum:
		count += pre_sum[curr_sum - target]

	# Remember the sum of all elements in every path
	# we've seen so far.
	if curr_sum not in pre_sum:
		pre_sum[curr_sum] = 1
	else:
		pre_sum[curr_sum] += 1

	helper(root.left, curr_sum, target, pre_sum)
	helper(root.right, curr_sum, target, pre_sum)

	# Clean up the effect of curr_sum when we're done with
	# this level of recursion.
	pre_sum[curr_sum] -= 1
```

## Comments

* `pre_sum` acts as a record of the path seen so far - more specifically, it stores the sum from the root to the current node
* What we’re interested in from this path is the subpath that starts from some middle node to the current node
	* If this subpath’s sum is equal to `target`, we want to count this subpath
* If we’re able to find the remainder of `curr_sum - target` in `pre_sum`, that means the remainder is (the sum of) a valid path until just before the start of `target`’s path

```
A -> B -> C -> D -> E
remainder/pre sum = {A, B, C}
target = {D, E}
curr sum = {A, B, C, D, E}
pre sum - target = curr sum
```

* There could be multiple subpaths that sum up to `target` - `pre_sum` encodes this info temporarily in its values
* The returning part of the recursion collects these values and sums them into the final result

* It took working through an example and drawing out the paths to have an initial understanding of how it works
* The LeetCode discussions were helpful in understanding the underlying math

* This solution is elegant in that it does many things with few lines of code
* The path building in `pre_sum` goes top-down, but the summing of the number of valid paths goes bottom-up
