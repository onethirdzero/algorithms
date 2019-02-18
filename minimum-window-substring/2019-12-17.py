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

import collections
import sys

class Solution:
    """
    https://xiufengchen.github.io/2016/03/11/String-Summary/

    - Runs in O(|s| + |t|) time.
    - Uses O(|s| + |t|) space.

    - The high level idea is to move the sliding window's right pointer right until the required condition is met, then move the left pointer right while the required condition is maintained.
    - The moment the required condition is not met, start moving the right pointer right again.
    - This pattern can be used for other constrained substring problems too.

    - The tricky part is understanding what the character counts mean.
        - If a character count is zero or negative, we don't need more of it in the current sliding window - a negative represents a surplus of that character.
        - Otherwise, a positive character count means we need more of it.
    - Because we've started `counts` off with positive counts of characters in t, all desired characters should have counts of 0 by the end of the algorithm, assuming that the desired substring exists.
        - I still don't understand why this works.
    """
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        # `counts` shows how many of its keys are desired.
        # `counts` starts off with all the characters in t.
        #
        # Part of the magic of Counter is that all keys that don't exist in it
        # automatically have a value of zero, giving us some syntactic sugar
        # over using a regular dictionary with the entire alphabet as its keys.
        counts = collections.Counter(t)

        desired = len(t)  # The number of desired characters to add to our sliding window.
        begin = end = head = 0
        d = sys.maxsize  # The length of the min substring.

        while end < len(s):
            # If the character we're about to include is desired.
            if counts[s[end]] > 0:
                # Decrement the number of desired characters.
                desired -= 1

            # If a desired character count is below zero, it means we have more
            # than enough of that character.
            # Undesired character counts will become negative and remain negative.
            counts[s[end]] -= 1
            # Move the right pointer right.
            end += 1

            # While we have all desired characters in our current sliding window.
            while desired == 0:
                # If our current sliding window is smaller than the min substring.
                if end - begin < d:
                    # Save the current sliding window as the new min substring.
                    head = begin
                    d = end - begin

                # Try to shrink the sliding window more.

                # If the character we're about to discard is a desired one.
                if counts[s[begin]] == 0:
                    # Increment the number of desired characters.
                    desired += 1

                # If a desired character count is above zero, it means we
                # need more of that character.
                # Undesired character counts will never increase above zero.
                counts[s[begin]] += 1
                begin += 1

        return "" if d == sys.maxsize else s[head:head + d]

    def test(self):
        assert self.minWindow('ADOBECODEBANC', 'ABC') == 'BANC'

        print('All tests passed!')

sol = Solution()
sol.test()
