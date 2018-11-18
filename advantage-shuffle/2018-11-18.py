#!/usr/bin/env python3

"""
https://leetcode.com/problems/advantage-shuffle

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

Example 1:
Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]

Example 2:
Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9


- Runs in O(n log n) time - sorting is our slowest operation.
- Uses O(n) space - we store all winners and losers in auxiliary data structures.
- The sorting shows us the smallest elements of A that can be used to beat B[j].
- If there are duplicate elements in B, the elements of A that beat these duplicates will be stored in the list keyed by B[j].
- If A[i] == B[j], A[i] is also a loser, because it won't beat any elements >= B[j].
"""


class Solution:
    # https://leetcode.com/problems/advantage-shuffle/solution/
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # Sort A and B.
        sortedA = sorted(A)
        sortedB = sorted(B)

        winners = {}
        losers = []

        # Compare them element-wise, recording winners and losers
        # in a dict.
        #
        # eg. A[i] beat B[j].
        # Store B[j] : [elements of A that beat B[j], A[i]].
        #
        # eg. A[i] doesn't beat B[j].
        # This means A[i] doesn't beat any other element >= B[j]. Store it as a loser.
        i = j = 0
        while i < len(sortedA):
            if sortedA[i] > sortedB[j]:
                # Record winner.
                if sortedB[j] in winners:
                    winners[sortedB[j]].append(sortedA[i])
                else:
                    winners[sortedB[j]] = [sortedA[i]]
                i += 1
                j += 1
            else:
                # Record loser. ie. A[i] <= B[j], so this handles duplicates.
                losers.append(sortedA[i])
                i += 1

        # Construct a new permutation of A based on elements of B,
        # which will consist of winners first, followed by losers.
        new_A = []

        for b in B:
            if b in winners and len(winners[b]) != 0:
                # Add from winners.
                new_A.append(winners[b].pop())
            else:
                # Add from losers.
                new_A.append(losers.pop())

        return new_A

    def test(self):
        # Duplicates in B.
        A = [2, 7, 12, 15, 10]
        B = [1, 9, 4, 11, 11]
        print(self.advantageCount(A, B))

        # A[i] == B[j].
        A = [2, 7, 11, 15, 10]
        B = [1, 9, 4, 11, 11]
        print(self.advantageCount(A, B))


sol = Solution()
sol.test()
