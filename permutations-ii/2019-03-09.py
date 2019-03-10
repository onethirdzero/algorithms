#!/usr/bin/env python3
"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

from typing import List

class Solution1:
    """
    https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)

    - Runs in O(n!) time.
        - There are n, n - 1, ..., 1 options when generating a permutation. So it takes O(n!) work to generate a single permutation. This has to be done for all n numbers in nums.
        - The sort costs O(n log n) time, but is negligible when considered under O(n!) time.
    - Uses O(n) space.

    - We sort nums so that we can reliably check whether nums[i - 1] is a duplicate of nums[i].
    """
    @classmethod
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perms, curr_perm, nums, used):
            if len(curr_perm) == len(nums):
                perms.append(curr_perm)
                return
            else:
                for i in range(len(nums)):
                    # If nums[i] is the same as nums[i - 1] and nums[i - 1] was not used.
                    if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                        continue

                    used[i] = True
                    backtrack(perms, curr_perm + [nums[i]], nums, used)
                    used[i] = False

        perms = []
        nums = sorted(nums)
        used = [False for _ in range(len(nums))]
        backtrack(perms, [], nums, used)

        return perms

class Solution2:
    """
    https://leetcode.com/problems/permutations-ii/discuss/18594/Really-easy-Java-solution-much-easier-than-the-solutions-with-very-high-vote/242059

    - Runs in O(n!) time.
        - There are n, n - 1, ..., 1 options when generating a permutation. So it takes O(n!) work to generate a single permutation. This has to be done for all n numbers in nums.
        - The shortening of nums on each recursive call costs O(n), since n - 1 elements need to be copied over into the new, shorter array.
        - The sort costs O(n log n) time, but is negligible when considered under O(n!) time.
    - Uses O(1) space on each recursive call.

    - We sort nums so that we can reliably check whether nums[i - 1] is a duplicate of nums[i].
    """
    @classmethod
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(perms, curr_perm, nums):
            # This can't be len(curr_perm) == len(nums) as before because
            # we're modifying curr_perm and nums on each recursive call,
            # so there isn't a stable value to compare each to.
            if len(nums) == 0:
                perms.append(curr_perm)
                return
            else:
                for i in range(len(nums)):
                    if i - 1 >= 0 and nums[i] == nums[i - 1]:
                        continue

                    backtrack(perms, curr_perm +
                              [nums[i]], nums[:i] + nums[i + 1:])

        perms = []
        nums = sorted(nums)
        backtrack(perms, [], nums)

        return perms

def test():
    perms = [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]

    assert Solution1.permuteUnique([1, 1, 2]) == perms
    assert Solution2.permuteUnique([1, 1, 2]) == perms

    print('All tests passed!')

test()
