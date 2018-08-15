# Longest Substring Without Repeating Characters - Sliding Window Optimized

* [Longest Substring Without Repeating Characters - LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

## Algorithm

* Previously, the hash table would only tell us about the existence of duplicates
* We can actually use it to also record a character’s index, so that we can skip the work of advancing `i` one by one when we hit a duplicate

* For `j` from `0` to `n - 1`
	* If `s[j]` in hash table
		* Jump `i` to `max(ht[s[j]], i)`
	* Update current longest to `max(length of current slice, current longest)`
	* Assign/update `s[j]: j + 1` in the hash table

## Complexity

* Time: `O(n)`
	* `j` visits each character only once - even in cases where `i` jumps, `j` continues advancing - no loop is wasted on advancing `i`
* Space: `O(min(m,n))` where `m` is the size of the charset/alphabet

## Comments

* Initially, I thought the algorithm would remain the same, since we’re only tweaking a small part of the sliding window idea
* Turns out that this small tweak changes the algorithm considerably
* When we skip advancing `i` one by one, we also skip deleting the previously recorded characters in the hash table (previously done by the `else` block) - this forces the algorithm to use a different looping structure
* Instead of the while loop which allowed either `i` or `j` to advance on each iteration, `j` is advanced on each loop even when `i` needs to jump - all work is done on a single pass
* Therefore, the answer is updated on each iteration, unlike previously where it was done only in the `if` block

* Assigning `s[j]: j + 1` to the hash table updates the index of the most recent duplicate - this is so that `i` starts at the most recent duplicate
* In other words, the values stored in the hash table are indices that we want `i` to start from if `s[j]` is a duplicate ie. the index after current `j`

* There can be a case where `i` is at a higher index than `ht[s[j]]` (the last recorded index of a duplicate)
	* In other words, the last encountered duplicate is below the sliding window
* In this case, we don’t want to assign `i` to that lower index, otherwise the resulting substring would contain duplicates
* Jumping `i` to `max(ht[s[j]], i)` instead of just `ht[s[j]]` prevents this
* This is an implementation detail, but it was something that puzzled me until I tested ‘abcba’
