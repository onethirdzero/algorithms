#!/usr/bin/env python

"""
https://leetcode.com/problems/spiral-matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


- Runs O(mn) time - we visit every cell once.
- Uses O(mn) space - size of the 'seen' matrix.
    - If we're allowed to modify the matrix in-place, we can mark each 'seen' cell as null, and check whether the candidate cell is null instead - this will use O(1) space for memoization, but we'll still incur O(mn) cost for storing the list of answers.
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None:
            return []

        rows, cols = len(matrix), len(matrix[0])
        seen = [[False] * cols for _ in range(rows)]
        answer = []

        # Directions that our cursor will move in.
        # Right, down, left, up.
        di_row = [0, 1, 0, -1]
        di_col = [1, 0, -1, 0]

        # di indicates which direction we'll step in.
        # It helps create next step we'll take in row and column space,
        # based on di_row and di_col's values.
        r = c = di = 0

        for _ in range(rows * cols):
            answer.append(matrix[r][c])
            seen[r][c] = True

            # Create candidate row and column.
            cr = r + di_row[di]
            cc = c + di_col[di]

            # If candidate is within bounds and not seen before.
            if 0 <= cr < rows and 0 <= cc < cols and not seen[cr][cc]:
                # Continue in that direction.
                r = cr
                c = cc
            else:
                # Change directions.
                di = (di + 1) % 4
                r = r + di_row[di]
                c = c + di_col[di]

        return answer

    def test(self):
        m1 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        assert self.spiralOrder(m1) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

        m2 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        assert self.spiralOrder(m2) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

        print('All tests pass!')


sol = Solution()
sol.test()
