"""
https://leetcode.com/problems/search-a-2d-matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3

Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13

Output: false
"""

class Solution:
    """
    https://leetcode.com/problems/search-a-2d-matrix/discuss/26201/A-Python-binary-search-solution-O(logn)
    https://leetcode.com/problems/search-a-2d-matrix/discuss/26219/Binary-search-on-an-ordered-matrix

    - Runs in O(mn log (mn)) time - binary search running time.
    - Uses O(1) space.

    - Because the matrix has sorted rows, we're essentially treating the matrix as a sorted array and doing a binary search.
    - The useful pattern here is the mapping from m x n matrix indices to array/1 x n matrix indicies.
        matrix[row_index][col_index] -> A[row_index * m + col_index]
    - Say we want index i in A, but in matrix indices. i / n gives us the number of rows we need to pass before we're on the correct row in matrix. Once we're on the correct row, i % n gives us the number of columns we need to pass before we're on the correct column in that row.
    - Using that, we know that the middle index of A is mid = m * n - 1. So in matrix terms, that's mid / n and mid % n.

    - Struggled with Python 3's true division (/) for a while because int() and math.ceil() rounded to the wrong integers, which resulted in IndexErrors.
    - Works fine with Python 3 floor division (//) or math.floor().

    - The middle index can also be found via bit shift by 1, but requires a little extra tweaking for off-by-one errors.
    """

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])
        begin = 0
        end = m * n - 1

        while begin <= end:
            mid = (begin + end) // 2
            mid_value = matrix[mid // n][mid % n]

            if mid_value == target:
                return True
            elif mid_value < target:
                # Look at right half.
                begin = mid + 1
            else:
                # Look at left half.
                end = mid - 1

        return False
