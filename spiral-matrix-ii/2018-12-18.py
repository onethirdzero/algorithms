#!/usr/bin/env python3

"""
https://leetcode.com/problems/spiral-matrix-ii

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


- Runs in O(n) time.
- Uses O(1) space.

- The solution is straightforward once you understand how to solve the original Spiral Matrix problem.
"""


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rows = cols = n
        di_row = [0, 1, 0, -1]
        di_col = [1, 0, -1, 0]

        # Generate an empty matrix.
        matrix = [[0 for c in range(cols)] for r in range(rows)]

        # Traverse spirally and fill the matrix.
        r = c = di = 0
        for i in range(rows * cols):
            matrix[r][c] = i + 1

            # Generate candidate cell.
            cr = r + di_row[di]
            cc = c + di_col[di]

            if 0 <= cr < rows and 0 <= cc < cols and matrix[cr][cc] == 0:
                r = cr
                c = cc
            else:
                # Change directions.
                di = (di + 1) % 4
                r = r + di_row[di]
                c = c + di_col[di]

        return matrix

    def test(self):
        assert self.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        print('All tests passed!')


sol = Solution()
sol.test()
