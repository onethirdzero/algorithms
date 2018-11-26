#!/usr/bin/env python3

"""
https://leetcode.com/problems/combination-sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

- Runs in exponential time - not sure how to break it down.
- Uses O(k / smallest candidate) space, where k is target?

- Python is a little trickier to backtrack with because it's pass by object reference.
    - If we modify current_solution by appending to it, we need to make sure it gets popped too at the end of the recursion too - I'm still not sure how to do this properly.
    - What I've fallen back to is passing current_solution + [candidate[i]] to the recursive call - this doesn't permanently mutate current_solution, but changes it enough to do the job - my guess is that current_solution is probably still [] at the end of all the recursion
"""


class Solution(object):
    # https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self._dfs(results, [], candidates, target, 0)

        return results

    def _dfs(self, results, current_solution, candidates, target, index):
        # Backtrack.
        if target < 0:
            return

        if target == 0:
            results.append(current_solution)
            return

        else:
            # Try more candidates.
            for i in range(index, len(candidates)):
                # We concatenate to current_solution instead of appending.
                # Taken from: https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.
                self._dfs(results, current_solution + [candidates[i]],
                                candidates, target - candidates[i], i)

    def test(self):
        print(self.combinationSum([2, 3, 6, 7], 7))


sol = Solution()
sol.test()
