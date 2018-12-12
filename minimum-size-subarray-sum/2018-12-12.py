#!/usr/bin/env python3

"""
https://leetcode.com/problems/minimum-size-subarray-sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum >= k. If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


- Runs in O(n) time - each element is visited at most twice.
- Uses O(1) space - we don't grow any data structures.

- We start off looking for all possible contiguous subarrays, but we trim the search space the moment we know that the current subarray is the shortest we'll ever see using the left index as the starting point.
- Similar to subset sum.
- The other solutions are good practice for incremental optimization.
"""


import sys

# https://leetcode.com/articles/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        answer = sys.maxsize
        i = left = curr_sum = 0

        for i in range(n):
            curr_sum += nums[i]

            # At this point, we have the shortest subarray we'll ever see
            # with left as the starting point.
            while (curr_sum >= s):
                # Update the min so far before moving left forward.
                answer = min(answer, i + 1 - left)

                curr_sum -= nums[left]
                left += 1

        return answer if answer != sys.maxsize else 0

    def test(self):
        assert self.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
        print('All tests passed!')


sol = Solution()
sol.test()
