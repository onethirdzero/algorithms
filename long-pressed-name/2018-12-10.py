#!/usr/bin/env python3

"""
https://leetcode.com/problems/long-pressed-name

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.

Note:
- name.length <= 1000
- typed.length <= 1000
- The characters of name and typed are lowercase letters.


- Runs in O(m + n) time - need to compare every element in `name` and `typed`.
- Uses O(1) space.

- The key point here is making sure that each contiguous block of a character in `typed` has a count of at least the count of the corresponding character block in `name`.
    - eg. name = 'abc', typed = 'aabbbcc' - each character in typed has a count of at least 1.
- Good pattern to know for character comparisons.
"""


class Solution:
    # https://leetcode.com/articles/long-pressed-name
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        for name_char in name:
            # If we haven't found a point to start matching
            # or aren't able to match all of name's characters.
            if i == len(typed):
                return False

            # If there's a mismatch.
            if typed[i] != name_char:
                # If it's the first character block of typed
                # or the character wasn't long pressed.
                if i == 0 or typed[i] != typed[i - 1]:
                    return False

                # Discard all similar characters until
                # the next different character.
                # ie. Skip all long pressed characters.
                curr = typed[i]
                while i < len(typed) and typed[i] == curr:
                    i += 1

                # The next different character must match
                # name's current character.
                if typed[i] != name_char:
                    return False
            i += 1

        return True

    def test(self):
        assert self.isLongPressedName('alex', 'aaleex') == True
        assert self.isLongPressedName('saeed', 'ssaaedd') == False
        assert self.isLongPressedName('leelee', 'lleeelee') == True
        assert self.isLongPressedName('laiden', 'laiden') == True
        print('All tests passed!')


sol = Solution()
sol.test()
