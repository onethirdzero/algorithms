#!/usr/bin/env python3

"""
https://leetcode.com/articles/set-matrix-zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
- A straight forward solution using O(mn) space is probably a bad idea.
- A simple improvement uses O(m + n) space, but still not the best solution.
- Could you devise a constant space solution?


- Runs in O(mn) time.
- Uses constant space.
- The trick is to set sentinel values in the first cell of the row and column that a cell is in - this works because the cells that contain sentinel values are cells that we've already visited, so we don't have to worry about overwriting their values.
- When setting sentinel values, we need to be careful to start looking at cell values starting from the second row and second column. If we start looking from the first row and first column, it's easy to corrupt the sentinel values, which often causes the entire matrix to be set to zero.
"""


class Solution():
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        set_first_col = False

        # Go through the matrix setting sentinel values.
        for row in range(rows):
            # Since the first cell of the first row and first column is the same
            # for matrix[0][0], we need an extra variable to contain the sentinel
            # value for it.
            # In this case, we use matrix[0][0] for the first row and
            # set_first_col for the first column.
            if matrix[row][0] == 0:
                set_first_col = True

            # We avoid looking at the first column because setting any sentinel
            # values here would cause the entire column to be set to zero later,
            # which in turn causes the entire matrix to be set to zero.
            for col in range(1, columns):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0 # Set sentinel value in the first cell of the current row.
                    matrix[row][0] = 0  # Set sentinel value in the first cell of the current column.

        # Go through the matrix again, updating rows and columns according
        # to sentinel values.
        # We avoid looking at the first row and first column because checking the
        # sentinel value in matrix[0][0] could corrupt the other sentinel values
        # in the first row and first column, causing the entire matrix to be
        # set to zero.
        for row in range(1, rows):
            for col in range(1, columns):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # Lastly, check if the first row and column need to be set to zero.
        if matrix[0][0] == 0:
            for col in range(columns):
                matrix[0][col] = 0

        if set_first_col:
            for row in range(rows):
                matrix[row][0] = 0

    def _printMatrix(self, m):
        for row in m:
            print(row)
        print('')

    def test(self):
        m1 = [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ]

        print('Input')
        self._printMatrix(m1)
        self.setZeroes(m1)
        print('Output')
        self._printMatrix(m1)

        m2 = [
            [0, 1, 2, 0],
            [3, 4, 5, 2],
            [1, 3, 1, 5]
        ]

        print('Input')
        self._printMatrix(m2)
        self.setZeroes(m2)
        print('Output')
        self._printMatrix(m2)

        m3 = [
            [1, 1, 1], [0, 1, 2]
        ]

        print('Input')
        self._printMatrix(m3)
        self.setZeroes(m3)
        print('Output')
        self._printMatrix(m3)


sol = Solution()
sol.test()
