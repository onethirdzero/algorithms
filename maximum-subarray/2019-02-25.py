#!/usr/bin/env python3
"""
https://leetcode.com/problems/maximum-subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

from typing import List

class Solution1:
    """
    https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts

    - Runs in O(n) time.
    - Uses O(n) space.

    - dp[i] represents the largest subarray sum from in nums[0:i].
    """
    @classmethod
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        max_subarray_sum = dp[0]

        for i in range(1, len(nums)):
            # If the previous slice had a positive sum, the sum of nums[i]
            # with it would yield a larger sum.
            if dp[i - 1] > 0:
                dp[i] = nums[i] + dp[i - 1]
            # Otherwise, the largest sum so far is just nums[i] itself/
            else:
                dp[i] = nums[i]

            max_subarray_sum = max(max_subarray_sum, dp[i])

        return max_subarray_sum

class Solution2:
    """
    https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts/185985

    - Runs in O(n) time.
    - Uses O(1) space.

    - We don't need the previous results of dp[i] after we've used it, so we can get by with just dp[i - 1] each time.
    """
    @classmethod
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = nums[0]
        max_subarray_sum = running_sum

        for i in range(1, len(nums)):
            # If adding the previous slice's sum to the current element
            # is better than just the current element.
            if running_sum + nums[i] >= nums[i]:
                running_sum += nums[i]
            else:
                running_sum = nums[i]

            max_subarray_sum = max(max_subarray_sum, running_sum)

        return max_subarray_sum

def test():
    assert Solution1.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution2.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    print('All tests passed!')

test()
