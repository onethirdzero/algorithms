# Product of All Numbers Excluding k - With Division

* Daily Coding Problem #2

“This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index `k` of the new array is the product of all the numbers in the original array except the one at `k`.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.

Follow-up: what if you can't use division?”

## Algorithm

* If the length of the list is less than `2`
	* Return the original list
* Take the product of all elements in the list - at the same time, count the number of `0`s
* If there are 2 or more `0`s - edge case
	* Return a new list of only `0`s
* For each element in the list
	* If there was only one `0` - edge case
		* If current element is `0`
			* Assign total product to the new list
		* Else
			* Assign `0` to the new list
	* Else - there are no `0`s
		* Divide the total product by the current element and assign it to the new list
* Return the new list

## Edge cases

* Empty list: `[]`
* List of only zeroes: `[0, 0, 0]` -> `[0, 0, 0]`
* List of only one zero: `[1, 0, 3, 4]` -> `[0, 12, 0, 0]`
* List of more than one zero: `[1, 0, 0, 4, 5]` -> `[0, 0, 0, 0, 0]`

## Complexity

* Time: `O(n)`
* Space: `O(n)` - size of the new list

## Comments

* The edge cases are very important for this problem - without them, the algorithm is deceivingly simple to verify for correctness
