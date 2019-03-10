#!/usr/bin/env python3
"""
https://leetcode.com/problems/permutations

Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

from typing import List

class Solution:
    # Based on :https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perms, curr_perm, nums):
            if len(nums) == 0:
                perms.append(curr_perm)
                return
            else:
                for i in range(len(nums)):
                    backtrack(perms, curr_perm +
                              [nums[i]], nums[:i] + nums[i + 1:])

        perms = []
        backtrack(perms, [], nums)

        return perms

    def test(self):
        perms = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
        assert self.permute([1, 2, 3]) == perms

        print('All tests passed!')


sol = Solution()
sol.test()
