# Coin Change - Dynamic Programming - Top Down

* [Coin Change - LeetCode](https://leetcode.com/problems/coin-change/solution/)

* Let `S` = amount
* Let `c` = coin denomination
* Let `x` = number of coins used of a given denomination

## Algorithm

* The problem’s substructure is defined by this relation:

```
F(S) = min num of coins needed to make change for amount S using coin denominations [c_0 ... c_n-1]

F(S) = F(S - C) + 1
```

* We don’t know what `C` is, so we compute `F(S - c_i)` for each `C` and take the min, which results in:
*
```
F(S) = min F(S - C) + 1, where S - C >= 0
F(S) = 0 when S = 0
F(S) = -1 when n = 0
```

* We then use a cache to answer solved subproblems in constant time

```py
def coinChange(coins, rem, count):
	# Base cases.
	if rem < 0: return -1
	if rem == 0: return 0

	# Look up solved subproblems.
	# TODO: What if a key doesn't exist yet?
	if count[rem - 1] != 0 return count[rem - 1]

	min_count = MAX_INT

	for coin in coins:
		res = coinChange(coins, rem - coin, count)

		# Filter valid and optimal subproblems.
		if res >= 0 and res < min_count:
			min = 1 + res

	count[rem - 1] = -1 if min == MAX_INT else min_count

	return count[rem - 1]
```

## Complexity

* Time: `O(S*n)`
	* In the worst case, `1` is the optimal solution to each subproblem - the recursive depth in this case would be `S`? - Not sure about this, actually
* Space: `O(S)`
	* Recursive depth of the tree in the worst case is `S`

## Comments

* At first, I thought this would just be the same as the brute force approach, but with caching
* Turns out, the way the problem is approached is completely different
* The recurrence relation and the expression of the problem’s substructure is essential to deriving the solution - it turns out more elegant than the brute force version
* We’re trusting that recursion will give us the optimal solution for each subproblem

* There is no slicing similar to the for loop in the brute force solution
* Instead, we rely on just the base cases to drive the movement through recursion - there is a deeper meaning to this that I’m not seeing right away with the recurrence relation

* It’s hard to follow the time and space complexity analysis because it’s a little obscured by recursion
