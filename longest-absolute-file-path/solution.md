# Longest Absolute File Path

* [Longest Absolute File Path - LeetCode](https://leetcode.com/problems/longest-absolute-file-path/description/)

## Prior Approach

* My approach was similar to the solution in that I used the number of tabs to track the depth of the current file
* However, I looked at one character at a time
	* The side effect of this is that I needed additional indices to segregate each word - this was tedious
* I also attempted to remember the value of the file path so far, which was not a requirement of the question
	* I did this with sometimes with previous questions as well - I’ll try to cut down on this and focus on just returning the desired type

## Solution

* [Longest Absolute File Path - LeetCode](https://leetcode.com/problems/longest-absolute-file-path/discuss/86619/Simple-Python-solution?page=1)

### Algorithm

* Split the string by `\n`
* For each word in list of words
	* Get the filename by stripping the word of `\t`
	* Calculate depth based on number of `\t`
	* If `.` is in word
		* Record `max(path len at current depth + current word, longest so far)`
	* Else
		* `Path len at current depth + 1 = path len at current depth + current word + 1`
* Return longest so far

```py
def longestFilePath(s):
	words = s.split()
	longest = 0
	path_len_so_far = {0: 0}
	for word in words:
		filename = word.strip('\t')
		depth = len(word) - len(filename) # Number of tabs.
		if '.' in word:
			longest = max(longest, path_len_so_far[depth] + len(word))
		else:
			path_len_so_far[depth + 1] = path_len_so_far[depth] len(word) + 1
```

## Analysis

* We update `path_len_so_far[depth + 1]` because it is based on the path length at our current depth

* Runs in `O(n)` time - we visit all words only once
* Uses `O(k)` space, where `k` is the max depth of the abstract file system
