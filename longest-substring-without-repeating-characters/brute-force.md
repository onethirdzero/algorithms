# Longest Substring Without Repeating Characters - Brute Force

* [Longest Substring Without Repeating Characters - LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

## Algorithm

* For `i` from 0 to `n - 1`
	* For `j` from `i + 1` to `n`
		* If each character in the current slice is not unique
			* If length of current slice - 1 > length of longest so far
				* Record new length of longest
* Return length longest

## Complexity

* Time: `O(n^3)`
	* Checking each character in the current slice for uniqueness is `O(n)`, so we effectively have 3 nested loops
* Space: `O(min(m, n))` where `m` is the size of the charset/alphabet
	* Either the string contains all `m` letters of the alphabet, or only a subset of it, `n`

## Comments

* Python hides the `O(n)` complexity of checking for uniqueness in its `if substring not in s` syntax, which was why I initially thought the algorithm was `O(n^2)` time complexity
