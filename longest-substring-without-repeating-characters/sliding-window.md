# Longest Substring Without Repeating Characters - Sliding Window

* [Longest Substring Without Repeating Characters - LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

## Algorithm

* Instead of incurring `O(n)` time for checking uniqueness, store each of the current slice’s characters in a hash table for `O(1)` lookup
	* This makes the algorithm run in `O(n^2)` time
* If we use a sliding window, the `O(n^2)` slicing of substrings can be made to run in `O(n)` time

* While `i < n` and `j < n`
	* If `s[j]` not in hash table
		* Assign `s[j]` to an arbitrary value in the hash table
		* Advance `j`
		* `longest = max(longest, j - i)`
	* Else
		* Delete `s[i]` in hash table
		* Advance `i`
* Return length of longest

## Complexity

* Time: `O(2n)` -> `O(n)`
	* In the worst case, each character is visited twice - once by `i`, once by `j`
* Space: `O(min(m, n))` where `m` is the size of the charset/alphabet

## Comments

* In the brute force approach, `j` advances till the end of the string for each `i`
* With the sliding window, `j` only advances till the end once - this avoids doing `O(n)` work for each iteration of `i`
* Another way to imagine it is that the sliding window ‘closes’ (`i = j`) fewer times, resulting in less overall work done

* Once we hit a duplicate, we remove `s[i]` and advance `i` forward until we pass the duplicate
	* Eventually, this removes the duplicate from the hash table, after which we start advancing `j` again
* When we hit a duplicate, we have the longest substring without repeating characters that starts from `i`, `s[i]` till `s[j-1]` (not Python slice syntax)
