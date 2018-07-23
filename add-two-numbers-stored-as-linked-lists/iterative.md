# Add Two Numbers Stored as Linked Lists

* https://leetcode.com/problems/add-two-numbers/solution/

* Note that the numbers are stored in reverse in the linked lists

## Algorithm

* Initialize `dummy` as the head of the new linked list
* Initialize `current` as first node of the new linked list
* Initialize `p` and `q` to heads of `L1` and `L2`
* `carry = 0`
* Loop until the end of `L1` and `L2`
	* `x = p.val` - if we’ve already hit the end of `L1`, `x = 0`
	* `y = q.val` - if we’ve already hit the end of `L2`, `y = 0`
	* `sum = x + y + carry`
	* `carry = int(sum / 10)`
	* `sum = sum % 10`
	* `current.val = sum`
	* `current = current.next`
* If `carry == 1`, add a new node with value of `1` at the end of the returning list - edge case
* Return `dummy`

## Edge cases

* 1 list is longer than the other
* 1 list is empty - though the original question assumes both lists are non-empty
* The result has an extra carry of `1` at the end

## Complexity

* Time: `O(max(m, n))`
* Space: `O(max(m, n) + 1)`

## Comments

* `carry` must be `0` or `1` because the largest possible sum between 2 digits is `9 + 9 + 1 = 19`
	* This assumption is why we know to add `1` if the resulting list has length `max(m, n) + 1` - edge case
	* eg. `99 + 1 = 100`

```
9 9
1   +
-----
0 0 1
```

* Seems like there’s no getting away from the `O(n)` time complexity of traversing a linked list

* Storing the numbers in reverse makes it intuitive to approach the calculation using elementary math
* Follow up: what if the linked lists stored the numbers in non-reverse order?

```
99 + 1 = 100

  9 9
+   1
-----
1 0 0
```
