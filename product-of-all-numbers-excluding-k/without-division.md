# Product of All Numbers Excluding k - Without Division

* Daily Coding Problem #2

“This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index `k` of the new array is the product of all the numbers in the original array except the one at `k`.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.

Follow-up: what if you can't use division?”

## Algorithm

* For `i` from `0` to `n-1`
	* `prod = 1`
	* For `j` from `0` to `n-1`
		* If not `j == i`
			* `prod = prod * lst[j]`
	* Assign `prod` to the new list
* Return the new list

## Complexity

* Time: `O(n^2)`
* Space: `O(n)`

## Comments

* I’m not sure how to optimize this without division
* However, the nice thing here is that there aren’t any edge cases
