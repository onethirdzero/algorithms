#!/usr/bin/env python3
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List
import sys

class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-:)-(In-case-if-interviewer-twists-the-input)/36818

    - Runs in O(n) time.
    - Uses O(1) space.
    """

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        # Calculate differences between adjacent pairs.
        diff = [0 for _ in range(len(prices) - 1)]
        for i in range(len(prices)):
            diff[i - 1] = prices[i] - prices[i - 1]

        # maxSubarray implements Kadane's algorithm.
        # Kadane's returns the sum of the subarray that results in max profit.
        # The start and end elements of that subarray yield max profit.
        #
        # Example that shows why it works:
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-:)-(In-case-if-interviewer-twists-the-input)/36798
        def maxSubarray(diffs: List[int]) -> int:
            if len(diffs) < 1:
                return 0

            current_max, max_so_far = 0, 0
            for i in range(len(diffs)):
                max_so_far = max(max_so_far, current_max + diffs[i])
                current_max = max(0, current_max + diffs[i])

            return max_so_far

        return maxSubarray(diff)

    def test(self):
        assert self.maxProfit([7, 1, 5, 3, 6, 4]) == 5
        assert self.maxProfit([7, 6, 4, 3, 1]) == 0

        print('All tests passed!')

sol = Solution()
sol.test()
