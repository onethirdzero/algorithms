# Coin Change - Brute Force with Backtracking

* [Coin Change - LeetCode](https://leetcode.com/problems/coin-change/solution/)

* Let `S` = amount
* Let `c` = coin denomination
* Let `x` = number of coins used of a given denomination

## Algorithm

* Enumerate all subsets of coin frequencies `[x_0 … x_n-1]` and take the minimum

```py
def coinChange(coin_index, coins, amount):
	if amount == 0: return 0

	# If we still have coins denominations and remainder on the amount.
	if coin_index < len(coins) and amount > 0:
		# Max num of coins in the current
		# denomination we can use.
		# ie. S/c_i
		max_num_of_curr_denom = amount / coins[coin_index]
		min_cost = MAX_INT

		# Slice the number of coins used in the
		# current denomination.
		for x in range(0, max_num_of_curr_denom):
			if amount >= x * coins[coin_index]:
				res = coinChange(coin_index, coins, amount - x * coins[coin_index])

				# If result is valid.
				if res != -1:
					min_cost = min(min_cost, res + x)

		return -1 if min_cost == MAX_INT else min_cost

return -1
```

## Complexity

* Time: `O(S^n)`
	* For each coin denomination, the most number of coins we could use is `S/c_i`
	* Since we have `n` denominations, `S/c_i` work is repeated `n` times - and since we recurse, work is multiplied `S/c_1 * S/c_2 ...`
* Space: `O(S)`
	* The max recursion depth is `n`, since we have `n` denominations

## Comments

* The main mechanisms that drive this algorithm are:
	* The moving through the coin denominations by the for loop
	* The slicing of the number of each coin denomination used by the recursion
* It’s still challenging to model the problem mathematically, but once you do, it’s easier to derive the algorithm
* This is inefficient because we consider every possible solution, so a lot of work is duplicated

* This is a variation of the backpack problem, but I don’t know which variant specifically - a comment on LeetCode mentioned it’s the ‘complete backpack problem’
