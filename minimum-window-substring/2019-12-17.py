#!/usr/bin/env python3
"""
https://leetcode.com/problems/minimum-window-substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
- If there is no such window in S that covers all characters in T, return the empty string "".
- If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


import sys

class Solution:
    """
    https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems

    https://xiufengchen.github.io/2016/03/11/String-Summary/
    """
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        # map contains the count of characters in t.
        map = {}
        for c in t:
            # Initialize the count of characters in t.
            if c in map:
                map[c] += 1
            else:
                map[c] = 1

        # The number of desired characters to add to our sliding window.
        counter = len(t)
        begin = end = head = 0
        d = sys.maxsize  # The length of the min substring.

        while end < len(s):
            # If the current character is desired.
            if s[end] in map and map[s[end]] > 0:
                # Decrement the number of desired characters.
                counter -= 1
                map[s[end]] -= 1

            # Move the right pointer right.
            end += 1

            # While we have all desired characters in our sliding window.
            while counter == 0:
                # If our current sliding window is smaller than the min substring.
                if end - begin < d:
                    # Save the current sliding window as the new min substring.
                    head = begin
                    d = end - begin

                # Try to shrink the sliding window more.

                # If the character we're about to discard is a desired one.
                if s[begin] in map and map[s[begin]] == 0:
                    # Increment the number of desired characters before
                    # moving the left pointer right.
                    counter += 1
                    map[s[begin]] += 1
                begin += 1

        return "" if d == sys.maxsize else s[head:head + d]

    def test(self):
        self.minWindow('ADOBECODEBANC', 'ABC') == 'BANC'

        print('All tests passed!')

sol = Solution()
sol.test()
