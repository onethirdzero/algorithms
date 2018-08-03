# Shuffle An Array - Fisher-Yates Algorithm

* https://leetcode.com/articles/shuffle-an-array/

## Algorithm

* For each index in `array`
	* Pick a random index between the current index and the last index
	* Swap the elements of the random index and the current index

## Comments

* This is the canonical algorithm for shuffling an array
* By swapping the elements in-place, we save on using an auxiliary copy of the array and `O(n)` list modification
