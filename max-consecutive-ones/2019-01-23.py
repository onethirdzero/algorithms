#!/usr/bin/env python3
"""
https://leetcode.com/problems/max-consecutive-ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:
- The input array will only contain 0 and 1.
- The length of input array is a positive integer and will not exceed 10,000


Comments:
- Took embarrassingly long to get my head around the edge cases.
- First question back after an unintentional break.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = max_count = 0

        for x in nums:
            if x == 1:
                count += 1
            else:
                count = 0

            max_count = max(max_count, count)

        return max_count
