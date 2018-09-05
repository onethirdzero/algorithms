# Largest Sum of Non-Adjacent Numbers - O(1) Space

“Daily Coding Problem #9

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
“

## Algorithm

* `incl` - sum of all previous non-adjacent elements including the previous element
* `excl` - sum of all previous non-adjacent elements excluding the previous element

* `incl = A[0] + A[1]`
* `excl = A[0]`
* For each element in the list starting from index `2`
	* `excl = excl + A[i]`
	* `incl = max(incl, excl)`
* Return `max(incl, excl)`

## Complexity

* Time: `O(n - 2)` -> `O(n)`
	* We visit each element only once
* Space: `O(1)` - no memoization table used

## Comments

* It’s helpful to picture the two sums like this:

```
[ ..., ..., ..., prev, curr, ...]
 |---- excl ---|
 |------ incl -------|
```

* We trust that the sums are made of non-adjacent numbers so far
* At each iteration, we’re just updating state
