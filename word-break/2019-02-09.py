#!/usr/bin/env python3
"""
https://leetcode.com/problems/word-break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution:
    """
    https://leetcode.com/problems/word-break/discuss/43808/Simple-DP-solution-in-Python-with-description

    - Runs in O(n * k) - where k is the size of the word dictionary.
    - Uses O(n) space.

    - d is an array that tracks which points in s can be broken.
    - d[i] is true if a word in the dictionary ends at index i, and d was also true at the beginning of this word.
        - ie. The current slice needs to be true at both ends.

    - s[i - len(word) + 1:i + 1] can sometimes have weird values like s[-3:1] - Python just returns an empty string in this case.

    - I don't see what part of this solution makes it DP.
    """
    def wordBreak(self, s: 'str', wordDict: 'List[str]') -> 'bool':
        d = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                # If the slice matches a word in the dictionary.
                if (word == s[i - len(word) + 1:i + 1] and
                        # If d was also true at beginning of the slice.
                        (d[i - len(word)] or
                        # Probably an edge case.
                        i - len(word) == -1)):
                    d[i] = True

        return d[-1]

    def test(self):
        assert self.wordBreak('leetcode', ['leet', 'code']) == True
        assert self.wordBreak('applepenapple', ['apple', 'pen']) == True
        assert self.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) == False

        print('All tests passed!')


sol = Solution()
sol.test()
