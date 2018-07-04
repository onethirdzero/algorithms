# Coin Change - Dynamic Programming - Bottom Up

* [Coin Change - LeetCode](https://leetcode.com/problems/coin-change/solution/)

* Let `i` or `S` = amount
* Let `c` = coin denomination
* Let `x` = number of coins used of a given denomination

## Algorithm

* To approach it iteratively, we think in a bottom up manner
* Before we can calculate `F(i)`, we need to compute all the minimum `x` for amounts up to `i`
	* ie. We set `i` as a target, but start `i` from `0` up to `n - 1`
*  Each iteration `i` of `F(i)` is computed as:

```
min of j = F(i - c_j) + 1, where j = 0...n-1
```

```py
max = amount + 1
# Fill a list with max values.
dp = [max for _ in range(amount)]
dp[0] = 0 # Base case.

# Start from 1 because we've already set a value for index 0.
# i represents the remainder. We consider each possible value of i.
# Start looking at F(i) from the smallest value of i.
for i in range(1, amount + 1):
	# Consider each coin denomination.
	for j in range(len(coins)):
		if coins[j] <= i:
			# If coin's denomination is enough to subtract from remainder, this is valid for calculation.
			# Start calculation by looking at F(i - denomination) + 1 and comparing it to the currently saved value of F(i).
			dp[i] = min(dp[i], dp[i - coins[j]] + 1)

# If F(i) was not successfully found, return -1.
# Otherwise, return F(i).
return -1 if dp[amount] > amount else dp[amount]
```

## Complexity

* Time: `O(S * n)`
	* Our memoization table is of size `S` and `n` work is done at each index, since we have `n` coins
* Space: `O(S)`
	* Memoization table is of size `S`

## Comments

* It seems that bottom up implies iteration and top down implies recursion
* It’s a little bit easier to understand the bottom up approach, since the basic idea is that we’re trying to fill a memoization table starting from small `i`
* With that realization in mind, it’s also easier to understand the time and space complexity - we can clearly see the work involved in filling the table

* The recurrence relation (if I can even call it that) seems identical to the top down approach, but something tells me that there’s a slight different - I don’t currently know what that is
