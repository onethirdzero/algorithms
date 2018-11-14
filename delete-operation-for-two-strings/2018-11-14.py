#!/usr/bin/env python3

"""
https://leetcode.com/problems/delete-operation-for-two-strings/description/

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""


class Solution1:
    """
    https://leetcode.com/problems/delete-operation-for-two-strings/solution/

    We know that if there are no common characters between the two words,
    we need m + n deletions to bring them both down to empty strings.

    If there is a LCS between them, then we need len(LCS) fewer deletions
    from both words.

    Therefore, the answer is m + n - 2 * len(LCS).

    - Runs in O(2^(max(m,n))) because of LCS - the recursion tree will
    have 2^(m+n) nodes.
    - Uses O(max(m,n)) space - depth of the recursion tree.
    """
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return len(word1) + len(word2) - 2 * self._lcs(word1, word2)

    def _lcs(self, s1, s2):
        """
        Returns the length of the LCS between s1 and s2 using recursion.
        """
        if len(s1) == 0 or len(s2) == 0:
            return 0
        if s1[-1] == s2[-1]:
            return self._lcs(s1[:-1], s2[:-1]) + 1
        else:
            return max(self._lcs(s1[:-1], s2), self._lcs(s1, s2[:-1]))

    def test(self):
        print(self.minDistance('sea', 'eat'))


class Solution2:
    """
    https://leetcode.com/problems/delete-operation-for-two-strings/solution/

    LCS's run time can be improved using memoization.

    - Runs in O(mn) time - time taken to fill up the memoization table.
    - Uses O(mn) space - size of the memoization table.
    """
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        return len(word1) + len(word2) - 2 * self._lcs(word1, word2, dp)

    def _lcs(self, s1, s2, dp):
        """
        Returns the length of the LCS between s1 and s2 using DP.
        """
        m = len(s1)
        n = len(s2)

        if m == 0 or n == 0:
            return 0
        # If an answer has already been computed from before.
        if dp[m][n] > 0:
            return dp[m][n]
        # If the last characters match.
        if s1[-1] == s2[-1]:
            dp[m][n] = self._lcs(s1[:-1], s2[:-1], dp) + 1
        # If the last characters don't match, consider cases where each is
        # deleted and take the max.
        else:
            dp[m][n] = max(self._lcs(s1[:-1], s2, dp), self._lcs(s1, s2[:-1], dp))

        return dp[m][n]

    def test(self):
        print(self.minDistance('sea', 'eat'))


sol1 = Solution1()
sol1.test()

sol2 = Solution2()
sol2.test()
