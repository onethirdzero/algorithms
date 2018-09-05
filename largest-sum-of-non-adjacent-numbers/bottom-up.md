# Largest Sum of Non-Adjacent Numbers - Bottom Up

“Daily Coding Problem #9

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
“

## Algorithm

* `M[-1] = 0`
* `M[0] = A[0]`
* For each element in the list, `A[i]`
	* Take the max of:
		* The largest sum of non-adjacent numbers in the slice `[0..i - 1]`
		* The largest sum of non-adjacent numbers in the slice `[0..i - 2]` + `A[i]`
	* Assign this max to a lookup table, `M`
* The answer we want is `M[n]`

## Complexity

* Time: `O(n)`
	* We do constant work to determine the new largest sum at each `i`, with half the work being economized by using a memoization table
* Space: `O(n)` - size of the memoization table

## Comments

* The memoization table encodes the largest sum of non-adjacent numbers in `A[0..i]`
* The indexing will take care of non-adjacency for us

```
[ ..., ..., i - 2, i - 1,  i , ...]
 |------ M[i - 1] ------|
 |----- M[i - 2] + A[i] -----|
```

* After that, it’s just a matter of choosing the largest number between them
* We can trust that the sum so far has only non-adjacent numbers - and we that choosing the max of these options will preserve that constraint

* I initially didn’t think that this was a DP problem - my mistake was only considering a single largest sum per subproblem
* This was only one half of the considerations - not enough to implement the mechanism for getting non-adjacent numbers
