# Longest Substring of k Unique Characters

## Problem

“Daily Coding Problem #13

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".”

## Brute Force Approach

### Algorithm

* Produce all possible substrings of a given string `s`
* Check for `k` unique characters in each one and return the longest substring with `k` unique characters

### Analysis

* Producing substrings takes `O(n^2)`
* eg. `abcba`
	* `5` substrings starting from ‘a’: ‘a’, ‘ab’, ‘abc’, ‘abcb’, ‘abcba’
	* `4` substrings starting from ‘b’
	* …
* `1 + 2 + ... + n = n(n+1)/2` -> `O(n^2)`
* Iterating through each string and counting the number of unique characters takes `O(n)` time
* So this approach takes `O(n^3)` time and `O(1)` space

## Sliding Window Approach

* [Find the longest substring with k unique characters in a given string - GeeksforGeeks](https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/)
* The solution is very similar to the one for ‘Longest substring of non-repeating characters’ - use a sliding window

### Algorithm

* Initialize a hash table `ht` and a variable for length of longest substring
* Let `i` and `j` be the left index and right index of the window respectively
* For `j` in `1..n`
	* Append `curr` to `slice`
	* If `curr` not in `ht`, add it with value `1`
	* Else, increment its count
	* If (number of keys in `ht` with value > 0) > `k`
		* Decrement `slice[i]` by 1 in `ht`
		* Move `i` rightwards by 1
	* If length of `slice` > longest substring so far, record length of `slice`
* Return length of longest substring

### Analysis

* Initially, I wanted to iterate through the current slice to check for the number of unique characters - this would have been `O(n)`
* By checking the hash table for number of keys instead, we get `O(k)` because the number of keys with value > 0 is upper bounded by `k`
* Therefore, checking the substring for validity takes constant time

* If we assume that inputs can only contain characters ‘a’ to ‘z’, then `k` is upper bounded by `26`

### Comments

* Before, I kept thinking that we would need to start a new substring each time the current character would break the validity of the current slice
* That stopped me from proceeding because I thought that approach would miss certain cases - couldn’t remember that the sliding window moves index by index at a time
