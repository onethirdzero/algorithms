#!/usr/bin/env python3

"""
https://leetcode.com/problems/reverse-words-in-a-string/description/

Given an input string, reverse the string word by word.

Example:
Input: "the sky is blue",
Output: "blue is sky the".

Note:
- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up: Try to solve it in-place in O(1) space.

- Runs in O(3n) -> O(n) time.
- Uses O(1) space.
    - The Python version of the solution isn't technically in-place, since we need to convert the given string to a list of characters in order to manipulate the string - but beyond that, we don't use any extra space.
- Good practice for manipulating strings using pointers.
- There wasn't a Python 3 option on this question.
"""


class Solution:
    # https://leetcode.com/problems/reverse-words-in-a-string/discuss/47720/Clean-Java-two-pointers-solution-(no-trim(-)-no-split(-)-no-StringBuilder)
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s.isspace():
            return ''

        # Convert string into a list so Python can mutate it.
        sChars = list(s)

        self._reverseString(sChars, 0, len(s) - 1)
        self._reverseWords(sChars)
        return self._cleanUpSpaces(sChars)

    def _reverseString(self, s, i, j):
        while i < j:
            # Swap.
            temp = s[j]
            s[j] = s[i]
            s[i] = temp

            # Move pointers.
            i += 1
            j -= 1

    def _reverseWords(self, s):
        n = len(s)
        i = j = 0

        while i < n:
            # (i < j) catches i up with j.
            # (i < n and s[i] is ' ') moves i to the start of a new word.
            while i < j or (i < n and s[i] is ' '):
                i += 1

            # (j < i) catches j up with i.
            # (j < n and s[j] is not ' ') moves j to the end of a word
            # started by i.
            while j < i or (j < n and s[j] is not ' '):
                j += 1

            # The last call to _reverseString will be when i == n -1.
            self._reverseString(s, i, j - 1)

    def _cleanUpSpaces(self, s):
        n = len(s)
        i = j = 0

        while j < n:
            # Move j to the start of a new word.
            while j < n and s[j] is ' ':
                j += 1

            # Copy characters backwards, from j to i.
            # If i == j, the string remains unchanged.
            while j < n and s[j] is not ' ':
                s[i] = s[j]
                i += 1
                j += 1

            if j < n:
                # Add a single space after the copied backward word,
                # in case there's a non-space where i was.
                # This does nothing if there was already a space
                # where i was.
                s[i] = ' '
                i += 1

        # Convert the subarray into a string, trim the trailing space and return.
        return ''.join(s[0:i]).rstrip()

    def test(self):
        print(repr(self.reverseWords('the sky is blue')))
        print(repr(self.reverseWords('  the   sky  is    blue  ')))
        print(repr(self.reverseWords('   ')))
        print(repr(self.reverseWords('   the')))

sol = Solution()
sol.test()
